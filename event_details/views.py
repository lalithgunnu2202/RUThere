from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from club_admin.models import *
from django.core.mail import send_mail

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
    send_mail(
            subject='Welcome to RUThere!',
            message=f'Hi {curr.username}, thanks for registering for {event}. This is a confirmation mail(do not reply). You  will receive a mail with final details an hour before the event.',
            from_email='lalithgunnu2202@gmail.com',
            recipient_list=[curr.email],
            fail_silently=False
        )
    messages.info(request,"You have been Successfully registered. Please Check Your mail for Confirmation Mail.")
    return render(request,'confirmation.html',{'event':event})