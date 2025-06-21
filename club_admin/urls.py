from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('home/', views.club_home_view, name='club_home'),
    path('create_event/', views.create_event_view, name='create_event'),
    path('club_attendees/', views.club_attendees, name='club_attendees'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
    path('delete_attendee/<int:attendee_id>', views.delete_attendee, name='delete_attendee'),
]