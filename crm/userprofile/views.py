from django.contrib.auth.forms import UserCreationForm #Will contain info on username, email and password
from django.shortcuts import render, redirect
from .models import UserProfile

# Create your views here.
def signup(request): 
    #checking if the form has been submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        #checking if the info is correct before saving it to the db
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user) #creating the user profile

            #redirecting to the login page
            return redirect('/log-in/')
    else: 
        form = UserCreationForm()
    
    return render(request, 'userprofile/signup.html', {'form': form})