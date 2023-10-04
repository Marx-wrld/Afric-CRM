from django import forms
from .models import Client, Comment, ClientFile

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'description')

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400', 
            'placeholder': 'Name'
            })
        )
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400', 
            'placeholder': 'Email'
            })
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400', 
            'placeholder': 'Description'
            })
        )

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400', 
            'placeholder': 'Comment'
            })
        )

class AddFileForm(forms.ModelForm):
    class Meta:
        model = ClientFile
        fields = ('file',)
    
    file = forms.CharField(
        widget=forms.FileInput(attrs={
            'class': 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400'
            })
        )