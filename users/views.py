from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import CustomUser

from .forms  import UserRegistrationForm, LoginForm

User = get_user_model()

def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(email=email,password=password)
        else:
            print(form.errors)
            return render(request, 'users/register.html', {'form': form})
        return redirect('users:home')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def term_of_service(request):
    return render(request, 'term.html')


def policy(request):
    return render(request, 'policy.html')
