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
            
            team = Team.objects.create(name='The Team Name', created_by=user) #creating the team
            team.members.add(user) #adding the members
            team.save()

            UserProfile.objects.create(user=user, active_team=team) #creating the user profile
            

            #redirecting to the login page
            return redirect('/login/')
    else: 
        form = SignUpForm()
    
    return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')  