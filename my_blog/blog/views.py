from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.

def homepage(request):
    posts = BlogPost.objects.all()  # Get all posts
    return render(request, 'blog/homepage.html', {'posts': posts})

def post_detail(request, id):
    # Use get_object_or_404 to retrieve a post by its id or return a 404 if not found
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})