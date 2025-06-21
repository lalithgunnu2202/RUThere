from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing_view'),
    path('get-started/', views.get_started, name='get_started'),
]