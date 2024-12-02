from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'peer w-full h-12 px-4 border border-gray-300 rounded-full focus:outline-none focus:border-primary transition duration-300 mb-4', 
            'placeholder': 'Username',
        }),
        label='',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'peer w-full h-12 px-4 border border-gray-300 rounded-full focus:outline-none focus:border-primary transition duration-300 mb-4',  
            'placeholder': 'Password',
        }),
        label='',
    )

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'peer w-full h-12 px-4 border border-gray-300 rounded-full focus:outline-none focus:border-primary transition duration-300 mb-4',  
            'placeholder': 'Username',
        }),
        label='',
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'peer w-full h-12 px-4 border border-gray-300 rounded-full focus:outline-none focus:border-primary transition duration-300 mb-4',  
            'placeholder': 'Password',
        }),
        label='',
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'peer w-full h-12 px-4 border border-gray-300 rounded-full focus:outline-none focus:border-primary transition duration-300 mb-4',  
            'placeholder': 'Confirm Password',
        }),
        label='',
    )
