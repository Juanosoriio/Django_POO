# Importar funciones de shortcuts de Django para renderizar, obtener objetos y redirigir
from django.shortcuts import render, get_object_or_404, redirect
# Importar el sistema de mensajes de Django
from django.contrib import messages
# Importar el modelo Pedido de la app actual
from .models import Pedido
# Importar el formulario PedidoForm del proyecto
from proyecto_pedidos.forms import PedidoForm

# Crear las vistas para las operaciones CRUD

"""

Este archivo contiene las vistas para la aplicación de pedidos.

"""

def listar_pedidos(request):
    """
    Vista para listar todos los pedidos.
    """
    pedidos = Pedido.objects.all()  # Obtener todos los pedidos de la base de datos
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})  # Renderizar la plantilla con la lista de pedidos

def crear_pedido(request):
    """
    Vista para crear un nuevo pedido.
    Si el método es POST, valida y guarda el formulario.
    """
    if request.method == 'POST':  # Si la solicitud es POST (envío de formulario)
        form = PedidoForm(request.POST)  # Crear formulario con datos POST
        if form.is_valid():  # Validar el formulario
            form.save()  # Guardar el nuevo pedido en la base de datos
            messages.success(request, 'Pedido creado exitosamente.')  # Mostrar mensaje de éxito
            return redirect('listar_pedidos')  # Redirigir a la lista de pedidos
    else:
        form = PedidoForm()  # Crear formulario vacío para GET
    return render(request, 'pedidos/crear_pedido.html', {'form': form})  # Renderizar plantilla con el formulario

def ver_pedido(request, pk):
    """
    Vista para ver los detalles de un pedido específico.
    """
    pedido = get_object_or_404(Pedido, pk=pk)  # Obtener el pedido por PK o 404 si no existe
    return render(request, 'pedidos/ver_pedido.html', {'pedido': pedido})  # Renderizar plantilla con detalles del pedido

def actualizar_pedido(request, pk):
    """
    Vista para actualizar un pedido existente.
    Si el método es POST, valida y guarda el formulario con la instancia existente.
    """
    pedido = get_object_or_404(Pedido, pk=pk)  # Obtener el pedido existente por PK
    if request.method == 'POST':  # Si es POST, actualizar
        form = PedidoForm(request.POST, instance=pedido)  # Formulario con datos POST y instancia existente
        if form.is_valid():  # Validar
            form.save()  # Guardar cambios
            messages.success(request, 'Pedido actualizado exitosamente.')  # Mensaje de éxito
            return redirect('listar_pedidos')  # Redirigir
    else:
        form = PedidoForm(instance=pedido)  # Formulario con datos del pedido para edición
    return render(request, 'pedidos/actualizar_pedido.html', {'form': form, 'pedido': pedido})  # Renderizar plantilla

def eliminar_pedido(request, pk):
    """
    Vista para eliminar un pedido.
    Confirma la eliminación antes de proceder.
    """
    pedido = get_object_or_404(Pedido, pk=pk)  # Obtener el pedido a eliminar
    if request.method == 'POST':  # Confirmación de eliminación
        pedido.delete()  # Eliminar el pedido
        messages.success(request, 'Pedido eliminado exitosamente.')  # Mensaje de éxito
        return redirect('listar_pedidos')  # Redirigir a la lista
    return render(request, 'pedidos/eliminar_pedido.html', {'pedido': pedido})  # Renderizar confirmación de eliminación
