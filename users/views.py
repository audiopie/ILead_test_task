from django.shortcuts import render, redirect
from .models import CustomUser
from .forms  import UserRegistrationForm

def register_view(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        return redirect('users:register')
    context = {
        'form': form,
    }
    return render(request, 'base.html', context)
