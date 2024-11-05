from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
   path('', views.login_page, name='login_page'),
   path('signup/', views.signup, name='signup'),
   path('register/', views.register, name="register"),
   path('log_in/', views.log_in, name='log_in'),
]