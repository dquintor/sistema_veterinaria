from django.db import models

class InformacionPersonal(models.Model):
    cedula = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    movil = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_rol

class RolesUsuario(models.Model):
    cedula = models.ForeignKey(InformacionPersonal, on_delete=models.CASCADE)  # Relación con InformacionPersonal
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)  # Relación con Rol

    class Meta:
        unique_together = ('cedula', 'id_rol')

    def __str__(self):
        return f"{self.cedula} - {self.id_rol.nombre_rol}"
