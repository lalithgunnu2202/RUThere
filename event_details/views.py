from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from club_admin.models import *
# Create your views here.
def event_details_view(request,event_id):
    foryous = Event_Details.objects.all()[:3]
    event = get_object_or_404(Event_Details,id=event_id)
    return render(request,'event_details.html',{'event':event,'foryous':foryous})

def confirmation_view(request,event_id):
    event = get_object_or_404(Event_Details,id=event_id)
    return render(request,'confirmation.html',{'event':event})

@login_required(login_url='login')
def register_view(request,event_id):
    curr = request.user
    event = get_object_or_404(Event_Details, id=event_id)
    registration = Registration.objects.create(event=event,student=curr)
    registration.save()
    messages.info(request,"You have been Successfully registered. We will send you a remainder before an hour for the event")
    return render(request,'confirmation.html',{'event':event})