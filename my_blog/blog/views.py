from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def homepage(request):
    # Query all blog posts from the database
    posts = BlogPost.objects.all()
    return render(request, 'blog/homepage.html', {'posts': posts})