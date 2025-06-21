from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('user_signup/', views.user_signup_view, name='signup'),
    path('user_login/', views.user_login_view, name='login'),
    path('user_logout/', views.user_logout_view, name='logout'),
]