from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, home_view

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('home', home_view, name='home'),
    path('', register_view, name='register')
]
