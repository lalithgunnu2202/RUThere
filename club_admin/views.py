from django.shortcuts import render,redirect
from event_details.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def club_home_view(request):
    return render(request,'club_home.html')

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
        return redirect('club_home')
    return render(request,'create_event.html')