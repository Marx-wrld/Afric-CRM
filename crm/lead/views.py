import csv
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from team.models import Team
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import AddCommentForm, AddFileForm
from client.models import Client, Comment as ClientComment

# Create your views here.
# Using class based views rather than function based views

@login_required
def leads_export(request):
    leads = Lead.objects.filter(created_by=request.user)

    #creating the Httpresponse object with the appropriate csv header

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="leads.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Client', 'Description', 'Created By', 'Created At'])

    #looping through all the clients
    for lead in leads:
        writer.writerow([lead.name, lead.description, lead.created_by, lead.created_at])

    return response

class LeadListView(LoginRequiredMixin, ListView): # list based view for leads list
    model = Lead
    
    #Using class based views - loginRequiredMixin instead of the decorator login_required

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, converted_to_client=False)

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  AddCommentForm()
        context['filesform'] = AddFileForm()

        return context
    
    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:list')
    
    def get_queryset(self):
        queryset = super(LeadDeleteView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status')
    success_url = reverse_lazy('leads:list')
    
    def get_context_data(self, **kwargs):
        context = super(LeadUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edit Lead'

        return context
    
    def get_queryset(self):
        queryset = super(LeadUpdateView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status')
    success_url = reverse_lazy('leads:list')
    
    def get_context_data(self, **kwargs):
        context = super(LeadCreateView, self).get_context_data(**kwargs)
        team = Team.objects.filter(created_by=self.request.user)[0]
        context['team'] = team
        context['title'] = 'Add Lead'

        return context

    def form_valid(self, form):
        team = Team.objects.filter(created_by=self.request.user)[0]

        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = team
        self.object.save()

        return redirect(self.get_success_url())

class AddFileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            file = form.save(commit=False)
            file.lead_id = pk
            file.team = team
            file.created_by = request.user
            file.save()

        return redirect('leads:detail', pk=pk)

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        form = AddCommentForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)
            comment = form.save(commit=False)
            comment.team = team.first()
            comment.created_by = request.user
            comment.lead_id = pk
            comment.save()

        return redirect('leads:detail', pk=pk)
    
class ConvertToClientView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        lead = get_object_or_404(Lead, created_by=request.user, pk=self.kwargs.get('pk'))
        team = Team.objects.filter(created_by=request.user)[0]

        client = Client.objects.create(
            name=lead.name,
            email=lead.email,
            description=lead.description,
            created_by=request.user,
            team=team,
        )
        
        lead.converted_to_client = True
        lead.save()

        #converting lead comments to client comments

        comments = lead.comments.all()

        for comment in comments:
            ClientComment.objects.create(
                content=comment.content,
                created_by=comment.created_by,
                team=comment.team,
                client=client,
            )

        #success message and redirect

        messages.success(request, 'Lead converted to client successfully')

        return redirect('leads:list')