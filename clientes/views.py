# clientes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cliente

# Crear Cliente
def crear_cliente(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        movil = request.POST.get('movil')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')

        if cedula and nombre and apellido and edad and direccion and telefono and movil and email and contrasena:
            try:
                Cliente.objects.create(
                    cedula=cedula,
                    nombre=nombre,
                    apellido=apellido,
                    edad=edad,
                    direccion=direccion,
                    telefono=telefono,
                    movil=movil,
                    email=email,
                    contrasena=contrasena
                )
                messages.success(request, 'Cliente registrado exitosamente.')
                return redirect('listar_clientes')
            except Exception as e:
                messages.error(request, f'Error al registrar cliente: {e}')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')

    return render(request, 'crear_cliente.html')

# Listar Clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

# Actualizar Cliente
def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.edad = request.POST.get('edad')
        cliente.direccion = request.POST.get('direccion')
        cliente.telefono = request.POST.get('telefono')
        cliente.movil = request.POST.get('movil')
        cliente.email = request.POST.get('email')
        cliente.contrasena = request.POST.get('contrasena')
        cliente.save()
        messages.success(request, 'Cliente actualizado exitosamente.')
        return redirect('listar_clientes')
    return render(request, 'actualizar_cliente.html', {'cliente': cliente})

# Eliminar Cliente
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('listar_clientes')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})

def home(request):
    return render(request, 'homescreen.html')