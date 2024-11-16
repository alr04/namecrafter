from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label="Enter Full Name Here: ", max_length=100)