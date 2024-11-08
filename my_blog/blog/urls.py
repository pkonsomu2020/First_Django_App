from django.urls import path
from . import views  # Import views from the blog app

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage route
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # URL for individual post detail
    path('post/add/', views.add_post, name='add_post'),  # URL for adding a new post
    path('post/edit/<int:id>/', views.edit_post, name='edit_post'),  # URL for editing a post
]