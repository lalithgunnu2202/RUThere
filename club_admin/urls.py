from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('home/', views.club_home_view, name='club_home'),
    path('create_event/', views.create_event_view, name='create_event'),
]