from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import AddPostView  # Import AddPostView only once
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage, post_list, post_detail, add_post, edit_post, delete_post

app_name = 'blog'

urlpatterns = [
    # Homepage route - Displays all posts
    path('', views.homepage, name='homepage'),

    path('', views.post_list, name='post_list'),  # You can keep this path to display the list of posts

    # URL for individual post detail - Displays a single post along with comments
    path('post/<int:id>/', views.post_detail, name='post_detail'),

    # URL for adding a new post - Class-based view for creating a new post
    path('post/add/', AddPostView.as_view(), name='add_post'),  # Class-based view

    # URL for editing a post - Function-based view for editing an existing post
    path('post/edit/<int:id>/', views.edit_post, name='edit_post'),

    # URL for deleting a post - Function-based view for deleting a post
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),

    # Admin route - URL for accessing the admin panel
    path('admin/', admin.site.urls),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', homepage, name='homepage'),
    path('posts/', post_list, name='post_list'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('add/', AddPostView.as_view(), name='add_post'),  # Use AddPostView here
    path('edit/<int:id>/', edit_post, name='edit_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)