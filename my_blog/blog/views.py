from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    posts = BlogPost.objects.all()  # Get all posts
    return render(request, 'blog/homepage.html', {'posts': posts})

def post_detail(request, id):
    # Use get_object_or_404 to retrieve a post by its id or return a 404 if not found
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post
            return redirect('homepage')  # Redirect to the homepage
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Add'})

def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # Update the existing post
            return redirect('post_detail', id=post.id)  # Redirect to the post's detail page
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit'})

def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.delete()  # Delete the post
        return redirect('homepage')  # Redirect to homepage after deletion
    return render(request, 'blog/delete_confirmation.html', {'post': post})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_post.html', {'form': form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('homepage')
    return render(request, 'blog/delete_confirmation.html', {'post': post})