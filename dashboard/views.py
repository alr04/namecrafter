from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# This part of the code is where the text that is displayed on the dashboard is stored.
@login_required
def homepage(request):
    return HttpResponse("Welcome to NameCrafter!")

@login_required
def about(request):
    return HttpResponse("About page.")