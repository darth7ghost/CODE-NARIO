from django import forms
from .models import Nota
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(max_length=75)
    apellido = forms.CharField(max_length=75)
    class Meta:
        model = User
        fields = ('username','nombre', 'apellido', 'password1', 'password2')
        field_classes = {'username': UsernameField}