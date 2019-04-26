from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings

from .models import CustomUser

from .forms  import UserRegistrationForm, LoginForm

User = get_user_model()

@login_required(login_url='users:login')
def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            newsletter = form.cleaned_data['newsletter']
            user = User.objects.create_user(email=email,password=password)
            if newsletter:
                send_mail('Thanks for join us!', 'You will be get our newsletter!',  settings.EMAIL_HOST_USER,
                [email], fail_silently=False)
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
