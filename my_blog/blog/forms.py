from django import forms
from .models import Post
from .models import Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']  # Fields to include in the form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']