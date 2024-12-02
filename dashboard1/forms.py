from django import forms


class NameForm(forms.Form):
    name = forms.CharField(max_length=100, label="Please Enter your Fullname", widget=forms.TextInput(attrs={'class': 'form-control'}))