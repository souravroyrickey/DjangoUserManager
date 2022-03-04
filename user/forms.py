import imp
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
from django import forms
from django.contrib.auth.models import Group


class CustomUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'password1', 'password2', 'role']

   
