from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='clientes_index'),  # Vista para la página principal de clientes
]
