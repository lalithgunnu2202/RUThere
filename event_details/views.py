from django.shortcuts import render , get_object_or_404
from .models import *
# Create your views here.
def event_details_view(request,event_id):
    foryous = Event_Details.objects.all()[:3]
    event = get_object_or_404(Event_Details,id=event_id)
    return render(request,'event_details.html',{'event':event,'foryous':foryous})

def confirmation_view(request,event_id):
    event = get_object_or_404(Event_Details,id=event_id)
    return render(request,'confirmation.html',{'event':event})