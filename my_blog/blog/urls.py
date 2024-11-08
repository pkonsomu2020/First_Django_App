from django.urls import path
from . import views  # Import views from the blog app

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage route
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # URL for individual post detail
]