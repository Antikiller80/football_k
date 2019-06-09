from django import forms
from django.forms import ModelForm
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        widgets = {
            'comments_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ваш комментарий: 400 символов"}),
        }