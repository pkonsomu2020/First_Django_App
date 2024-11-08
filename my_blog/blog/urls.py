from django.urls import path
from . import views  # Import views from the blog app
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage route
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # URL for individual post detail
    path('post/add/', views.add_post, name='add_post'),  # URL for adding a new post
    path('post/edit/<int:id>/', views.edit_post, name='edit_post'),  # URL for editing a post
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),  # URL for deleting posts
    path('admin/', admin.site.urls),  # Only one instance of the admin URL
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]