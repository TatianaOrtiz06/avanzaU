from django.shortcuts import render

def login_views(request):
    return render(request, 'login.html')