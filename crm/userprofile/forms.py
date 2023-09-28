from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400', 
            'placeholder': 'Username'
            })
        )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400',  
            'placeholder': 'Password'
            })
        )