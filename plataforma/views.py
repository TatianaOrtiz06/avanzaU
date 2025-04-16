from django.shortcuts import render
from .views.auth_views import login_view, register_view
from .views.dashboard_views import dashboard_view 

from django.shortcuts import render
def inicio(request):
    return render(request, 'inicio.html')
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')
def dashboard_view(request):
    return render(request, 'dashboard.html')
