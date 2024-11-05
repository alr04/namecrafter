from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login
from dashboard import views



def login_page(request):
    return render(request, 'login/login.html')

def signup(request):
    return render(request, 'login/signup.html')

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('password2')     
    if password != confirm_password:
        messages.error(request, "Passwords do not match")
        return render(request, 'login/signup.html')

    newUser = User(username=username)
    newUser.set_password(password)
    newUser.save()
    messages.success(request, 'Registered successfully!')
    return render(request, 'login/login.html')


def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "You have logged in successfully!")
        return redirect(views.homepage) 
    else:
         messages.error(request, "Invalid username or password.")
         return render(request, 'login/login.html')
 
    
