from django import forms
from .models import Client

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
