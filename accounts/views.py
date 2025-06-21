from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate ,login ,logout
user = get_user_model()

# Create your views here.
def user_signup_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        if user.objects.filter(username=username).exists():
            messages.error(request,"User already exists try logging in")
            return redirect('signup')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1!=password2:
            messages.error(request,"Your Passwords are not matching")
            return redirect('signup')
        email = request.POST.get('email')
        role = request.POST.get('role')
        new_user = user.objects.create_user(name=name,username=username,password=password1, email=email, role=role)
        new_user.save()
        messages.info(request,"You are logged in Automatically.")
        if role=='club':
            return redirect('club_home')
        else:
            return redirect('student_home')
        
    return render(request,'signup.html')

def user_login_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('get_started')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = authenticate(request,username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            messages.success(request, "You have successfully logged in!")
            if new_user.role=='club':
                return redirect('club_home')
            else:
                return redirect('student_home')
        else:
            # Generic error message - don't reveal if user exists
            messages.error(request, "Invalid username or password")
            return redirect('login')
    
    return render(request,'login.html')

def user_logout_view(request):
    logout(request)
    messages.info(request,"You have been Logged Out Successfully")
    return redirect('landing_view')