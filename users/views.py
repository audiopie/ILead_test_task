from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib import messages

from .forms  import UserRegistrationForm

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            pass
        else:
            print(form.errors)
            return render(request, 'base.html', {'form': form})
        return redirect('users:register')

    else:
        form = UserRegistrationForm()
    return render(request, 'base.html', {'form': form})
