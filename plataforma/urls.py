from django.urls import path
from plataforma.views import inicio_views, auth_views, dashboard_views

urlpatterns = [
    path('', inicio_views.inicio, name='inicio'),
    path('login/', auth_views.login_view, name='login'),
    path('registro/', auth_views.registro_view, name='registro'),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
]
