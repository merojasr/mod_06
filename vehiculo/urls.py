from django.urls import path
from vehiculo.views import *
from . import views

urlpatterns = [
    path('add/', views.agregar_vehiculo, name='add'),
    path('index/', views.index, name='index'),
    path('listar/', views.listar_vehiculos, name='listar'),
    path('', views.index, name='index'),
    
]