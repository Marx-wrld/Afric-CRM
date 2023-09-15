from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import AddClientForm
from django.contrib import messages
from team.models import Team

# Create your views here.


@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)

    return render(request, "client/clients_list.html", {"clients": clients})


@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    return render(request, "client/clients_detail.html", {"client": client})


@login_required
def clients_add(request):
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            client = form.save(commit=False)
            client.created_by = request.user
            client.team = team
            client.save()

            messages.success(request, "Client added successfully")

            return redirect("clients_list")
    else:
        form = AddClientForm()

    return render(request, "client/clients_add.html", {"form": form})


@login_required
def clients_edit(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'Client updated successfully')

            return redirect('clients_list')
    else:
        form = AddClientForm(instance=client)
    
    return render(request, 'client/clients_edit.html', {
        'form': form
    })


@login_required
def clients_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()

    messages.success(request, "Client deleted successfully")

    return redirect("clients_list")
