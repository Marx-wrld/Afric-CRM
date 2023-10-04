from django import forms
from .models import Comment, Lead, LeadFile

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status')

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
        model = LeadFile
        fields = ('file',)

    file = forms.CharField(
        widget=forms.FileInput(attrs={
            'class': 'form-control mb-6 my-4 w-full py-4 px-6 rounded-xl bg-gray-100 border border-gray-200 placeholder-gray-500 focus:outline-none focus:border-gray-400'
            })
        )