from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing_view(request):
    return render(request,'landing.html')

@login_required(login_url='signup')
def get_started(request):
    current_user = request.user
    if current_user.role=='club':
        return redirect('club_home')
    else:
        return redirect('student_home')