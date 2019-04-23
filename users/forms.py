from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}),required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    newsletter = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'checked':''}))



    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1','password2', 'newsletter')
