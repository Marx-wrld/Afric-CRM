from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASS = 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400', 

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASS, 
            'placeholder': 'Username'
            })
        )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': INPUT_CLASS,  
            'placeholder': 'Password'
            })
        )

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASS, 
            'placeholder': 'Username'
            })
        )
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASS, 
            'placeholder': 'Email'
            })
        )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': INPUT_CLASS,  
            'placeholder': 'Password'
            })
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':  INPUT_CLASS,  
            'placeholder': 'Confirm Password'
            })
        )