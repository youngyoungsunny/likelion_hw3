from django import forms
from .models import Blog, Comment

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
        #files = forms.FileField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

