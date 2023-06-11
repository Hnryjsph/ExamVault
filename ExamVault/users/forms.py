"""
You can add gender, email, other fields as required
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

GENDER_CHOICES = (
    ('1', 'male'),
    ('2', "female")
)


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    #gender = forms.ChoiceField(choices = GENDER_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)



