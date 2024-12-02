from django import forms

class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(max_length=150, label="New Username")

class QueryForm(forms.Form):
    query = forms.CharField(max_length=100, label="Input your desired destiny number here", widget=forms.TextInput())