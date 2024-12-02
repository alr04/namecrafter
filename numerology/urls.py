from django.urls import path
from . import views
from numerology import views


app_name = 'numerology'
urlpatterns = [
    path('', views.name_input, name='name_input'),
    path('result/', views.numerology_result, name='numerology_result'),
]