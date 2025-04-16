# plataforma/views/auth_views.py
from django.shortcuts import render, redirect


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def registro_view(request):
    return render(request, 'registro.html')

def forgot_password_view(request):
    return render(request, 'forgot_password.html')

