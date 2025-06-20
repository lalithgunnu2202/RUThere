from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('rsvp/', views.rsvp_view, name='rsvp_view'),
]