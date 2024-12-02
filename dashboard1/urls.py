from django.urls import path
from . import views

#app_name = 'dashboard'
app_name = 'dashboard1'
urlpatterns = [
    path('', views.homepage, name='homepage'),  # I’m naming this URL 'homepage' for easy reference.
    path('about/', views.about, name='about'),  # I’m naming this URL 'about' for easy reference.
    
]