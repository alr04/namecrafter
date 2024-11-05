from django.http import HttpResponse

# This part of the code is where the text that is displayed on the dashboard is stored.
def homepage(request):
    return HttpResponse("Welcome to NameCrafter!")


def about(request):
    return HttpResponse("About page.")