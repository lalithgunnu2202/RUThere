from django.shortcuts import render

# Create your views here.
def rsvp_view(request):
    return render(request,'rsvp.html')