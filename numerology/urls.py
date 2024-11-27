from django.urls import path
from . import views
from numerology import views

urlpatterns = [
    path('', views.name_input_view, name='name_input'),
    path('result/', views.numerology_result, name='numerology_result'),
]