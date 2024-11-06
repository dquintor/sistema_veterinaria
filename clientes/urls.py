# clientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('', views.listar_clientes, name='listar_clientes'),
    path('actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
]
