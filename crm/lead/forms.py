from django import forms
from .models import Comment, Lead

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status')

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)