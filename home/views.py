from django.shortcuts import render
from event_details.models import *
from .models import *

# Create your views here.
def student_home_view(request):
    clubs = Club.objects.all()
    events = Event_Details.objects.all()
    return render(request,'home.html',{'clubs':clubs,'events':events})
