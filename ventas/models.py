from django.db import models
from inventario.models import Producto  # Importamos Producto desde inventario
from clientes.models import Cliente  # Importamos Cliente desde clientes

class MetodoPago(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.descripcion

class VentaEncabezado(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con Cliente
    fecha_venta = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.id_cliente}"

class VentaDetalle(models.Model):
    id_venta = models.ForeignKey(VentaEncabezado, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con Producto
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('id_venta', 'id_producto')

    def __str__(self):
        return f"Detalle de venta {self.id_venta} - Producto: {self.id_producto}"

class HistorialVentas(models.Model):
    id_venta = models.ForeignKey(VentaEncabezado, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Historial de venta {self.id_venta}"

class Transaccion(models.Model):
    id_venta = models.ForeignKey(VentaEncabezado, on_delete=models.CASCADE)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado_transaccion = models.CharField(max_length=50)  # Ej: "pendiente", "completada"

    def __str__(self):
        return f"Transacción {self.id_venta} - Estado: {self.estado_transaccion}"
