from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('home')
    


def log_user_out(request):
    logout(request)
    return redirect('login')