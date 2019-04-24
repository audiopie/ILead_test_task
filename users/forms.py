from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import CustomUser

User = get_user_model()

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

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exist():
            raise ValidationError('This email already taken')
        return email
