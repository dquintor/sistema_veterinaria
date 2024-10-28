from django.db import models
from django.apps import apps

class Cliente(models.Model):
    cedula = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class HistorialCompras(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con Cliente
    id_venta = models.ForeignKey('ventas.VentaEncabezado', on_delete=models.CASCADE)  # Relación diferida
    fecha_compra = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Compra realizada por {self.id_cliente.nombre} el {self.fecha_compra}"
