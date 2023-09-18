from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Team
from .forms import TeamForm
from django.contrib import messages

# Create your views here.
@login_required
def edit_team(request, pk):
    team  = get_object_or_404(Team, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes were saved successfully!')

            return redirect('myaccount')
    else:
        form = TeamForm(instance=team)

    return render(request, 'team/edit_team.html', {
        'team': team,
        'form': form
    })