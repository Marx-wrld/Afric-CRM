from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from team.models import Team

# Create your views here.
def signup(request): 
    #checking if the form has been submitted
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        #checking if the info is correct before saving it to the db
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user) #creating the user profile
            
            team = Team.objects.create(name='The Team Name', created_by=request.user) #creating the team
            team.members.add(request.user) #adding the members
            team.save()

            #redirecting to the login page
            return redirect('/log-in/')
    else: 
        form = SignUpForm()
    
    return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]
    return render(request, 'userprofile/myaccount.html', {
        'team': team
    })  