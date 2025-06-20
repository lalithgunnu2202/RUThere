from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('student/', views.student_home_view, name='student_home'),
]