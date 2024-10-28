"""
URL configuration for sistema_veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def home(request):
    return HttpResponse('Bienvenido a la Veterinaria')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/',include('inventario.urls')),
    path('', home),
    path('ventas/', include('ventas.urls')),          
    path('compras/', include('compras.urls')),       
    path('clientes/', include('clientes.urls')),     
    path('administracion/', include('administracion.urls')),
]