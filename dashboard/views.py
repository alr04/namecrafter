from django.http import HttpResponse
# This part of the code is where the text that is displayed on the dashboard is stored.
def homepage(request):
    return HttpResponse("Welcome to NameCrafter!")

def other(request):
    return HttpResponse("Maybe there'll be another page here.")