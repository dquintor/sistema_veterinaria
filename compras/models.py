from django.db import models
from inventario.models import Producto  # Importamos Producto desde inventario

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class CompraEncabezado(models.Model):
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Compra {self.id} de {self.id_proveedor.nombre}"

class CompraDetalle(models.Model):
    id_compra = models.ForeignKey(CompraEncabezado, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con Producto
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('id_compra', 'id_producto')

    def __str__(self):
        return f"Detalle de compra {self.id_compra} - Producto: {self.id_producto}"
