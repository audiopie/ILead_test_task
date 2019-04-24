from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib import messages

from .forms  import UserRegistrationForm

User = get_user_model()

def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['first_name']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email,password=password)
        else:
            print(form.errors)
            return render(request, 'register.html', {'form': form})
        return redirect('users:home')

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
