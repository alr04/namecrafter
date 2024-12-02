from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "account"
urlpatterns = [
    path('', views.account_page, name='account_page'),
    path('logout/', LogoutView.as_view(next_page='login:login'), name='logout'),
    path('delete/', views.delete_account, name='delete_account'),
]
