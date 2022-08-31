from socket import fromshare
from tkinter import Widget
from django import forms
from .models import Post, Comment


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body',]


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4})
        }
        labels ={
            'body':'comment'
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
        widgets = {
            'body':forms.Textarea(attrs={'rows':2})
        }


class PostSearchForm(forms.Form):
    search = forms.CharField()
