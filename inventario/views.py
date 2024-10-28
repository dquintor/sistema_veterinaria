from django.http import HttpResponse
from django.shortcuts import render

# Vista para mostrar una lista de productos
def lista_productos(request):
    return HttpResponse("Aquí estará la lista de productos")

# Vista para mostrar detalles de un producto
def detalle_producto(request, producto_id):
    return HttpResponse(f"Detalles del producto con ID {producto_id}")
