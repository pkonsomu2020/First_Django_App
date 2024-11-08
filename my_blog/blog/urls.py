from django.urls import path
from . import views  # Import views from the blog app

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Point this to your homepage view
]