from typing import Any
from django import http
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from .models import Lead
from django.contrib import messages  
from client.models import Client
from team.models import Team
from django.views.generic import ListView, DetailView

# Create your views here.
# Using class based views rather than function based views

class LeadListView(ListView): # list based view for leads list
    model = Lead
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, converted_to_client=False)

class LeadDetailView(DetailView):
    model = Lead

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, 'Lead deleted successfully')

    return redirect('leads:list')

@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method  == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'Lead updated successfully')

            return redirect('leads:list')
    else:
        form = AddLeadForm(instance=lead)
    
    return render(request, 'lead/leads_edit.html', {
        'form': form
    })

@login_required
def add_lead(request):
    team = Team.objects.filter(created_by=request.user)[0]
    
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = team
            lead.save()

            messages.success(request, 'Lead added successfully')

            return redirect('dashboard')
    else:
         form = AddLeadForm()

    return render(request, 'lead/add_lead.html', {
        'form': form,
        'team': team
    })

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
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

    messages.success(request, 'Lead converted to client successfully')
  
    return redirect('leads:list')