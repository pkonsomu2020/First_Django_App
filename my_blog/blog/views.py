from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm, PostForm  # Only import PostForm now
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Home page view: Displays a list of all blog posts
def homepage(request):
    posts = Post.objects.all()  # Get all posts
    return render(request, 'blog/homepage.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all()  # Get all posts
    return render(request, 'blog/post_list.html', {'posts': posts})

# Post detail view: Displays the individual post with its comments
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Get post by ID or return 404 if not found
    comments = post.comments.all()  # Fetch all comments related to the post
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()  # Save the comment
            return redirect('blog:post_detail', id=post.id)  # Redirect to the same post detail page
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# Add a new post view (requires login)
@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Handle the form data
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet
            post.author = request.user  # Set the logged-in user as the author
            post.save()  # Save the post with the author set
            return redirect('post_list')  # Redirect to post list or another page
    else:
        form = PostForm()  # Create an empty form for GET requests
    return render(request, 'blog/add_post.html', {'form': form})

# Edit an existing post view (requires login)
@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Use PostForm here as well
        if form.is_valid():
            form.save()  # Update the existing post
            return redirect('blog:post_detail', id=post.id)  # Redirect to the post's detail page
    else:
        form = PostForm(instance=post)  # Use PostForm here as well
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit'})

# Delete a post view (requires login)
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()  # Delete the post
        return redirect('blog:homepage')  # Redirect to homepage after deletion
    return render(request, 'blog/delete_confirmation.html', {'post': post})


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list after successful creation