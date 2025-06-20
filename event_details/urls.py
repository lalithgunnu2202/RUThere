from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('<int:event_id>/', views.event_details_view, name='event_details'),
    path('confirm/<int:event_id>/', views.confirmation_view, name='confirmation'),
]