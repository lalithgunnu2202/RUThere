from django.shortcuts import render,redirect, get_object_or_404
from event_details.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def club_home_view(request):
    current_user = request.user
    if current_user.role=='club':
        registered = Registration.objects.filter(event__host=current_user).count()
        events = Event_Details.objects.filter(host=current_user).annotate(reg_count=Count('registrations'))
        return render(request,'club_home.html',{'events':events,'registered':registered,'curr':current_user})

@login_required(login_url='login')
def create_event_view(request):
    if request.method=='POST':
        name = request.POST.get('name')
        about = request.POST.get('about')
        date = request.POST.get('date')
        location = request.POST.get('location')
        time = request.POST.get('time')
        img_url = request.POST.get('img_url')
        price = request.POST.get('price')
        host = request.user
        event = Event_Details.objects.create(name=name,about=about,date=date,location=location,time=time,img_url=img_url,price=price, host=host)
        event.save()
        messages.info(request,"Event Created Successfully")
        return redirect('club_home')
    return render(request,'create_event.html')

@login_required(login_url='login')
def delete_event(request,event_id):
    event = get_object_or_404(Event_Details,id=event_id)
    event.delete()
    messages.info(request,"Event Deleted Successfully")
    return redirect('club_home')

@login_required(login_url='login')
def club_attendees(request):
    curr = request.user
    attendees = Registration.objects.filter(event__host=curr)
    return render(request,'attendees.html',{'attendees':attendees,'curr':curr})

@login_required(login_url='login')
def delete_attendee(request,attendee_id):
    attendee=get_object_or_404(Registration,id=attendee_id)
    attendee.delete()
    messages.info(request,"Attendee removed Successfully")
    return redirect('club_attendees')