from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
   path('', views.log_in, name='login'),
   path('signup/', views.signup, name='signup'),
]