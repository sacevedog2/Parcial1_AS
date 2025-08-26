from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.flight_create, name='create'),
    path('listar/', views.flight_list, name='list'),
    path('estadisticas/', views.flight_stats, name='stats'),
]
