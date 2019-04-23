from django import forms
from django.forms import ModelForm
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'last_name', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class':'form-control','type' : 'email', 'placeholder': 'Email'})
        }

    def clean_password(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["Password don't match"],
            )
        return password2
            
