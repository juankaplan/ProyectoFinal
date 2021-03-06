import email
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label= "Usuario")
    password1 = forms.CharField(label = "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
    

    
    