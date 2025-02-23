""" Defines URL patterns for users"""
from django.urls import path 
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Login page
    path(r'login/', LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'register/', views.register, name='register'),
]
