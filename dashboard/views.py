from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .models import UserActionLog  # Only import UserActionLog from models

# This part of the code is where the text that is displayed on the dashboard is stored.
@login_required
def homepage(request):
    # I’m fetching the recent logs for the logged-in user to display on the homepage.
    recent_logs = UserActionLog.objects.filter(user=request.user).order_by('-timestamp')[:10]
    # I’m logging that the user accessed the homepage.
    UserActionLog.objects.create(user=request.user, action="Viewed Homepage")
    # I’m rendering the home.html template and passing recent_logs to it.
    return render(request, 'dashboard/home.html', {'recent_logs': recent_logs})

@login_required
def about(request):
    # I’m logging that the user accessed the about page.
    UserActionLog.objects.create(user=request.user, action="Viewed About Page")
    return HttpResponse("About page.")
