from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .views import register_view, home_view, term_of_service, policy

app_name='users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('home', home_view, name='home'),
    path('term_of_service', term_of_service, name='term'),
    path('policy', policy, name='policy'),
    path('', register_view, name='register')
]
