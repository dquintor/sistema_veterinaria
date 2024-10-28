


from django.urls import path
from . import views  # Importamos las vistas definidas en views.py

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),  # Ruta para la lista de productos
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),  # Ruta para el detalle de un producto
]
