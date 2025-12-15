# Importar el módulo models de Django para definir modelos de base de datos
from django.db import models
# Importar validadores para campos de modelo
from django.core.validators import MinValueValidator, MinLengthValidator

# Crear tus modelos aquí.

"""

Este archivo define los modelos de la aplicación de pedidos.

"""

class Pedido(models.Model):
    """
    Modelo que representa un pedido realizado por un cliente.
    """

    # Opciones para el estado del pedido
    ESTADOS_CHOICES = [
        ('pendiente', 'Pendiente'),  # Estado inicial del pedido
        ('procesando', 'Procesando'),  # Pedido en proceso de preparación
        ('enviado', 'Enviado'),  # Pedido enviado al cliente
        ('entregado', 'Entregado'),  # Pedido entregado exitosamente
        ('cancelado', 'Cancelado'),  # Pedido cancelado
    ]

    cliente = models.CharField(max_length=100, validators=[MinLengthValidator(3, message='El nombre del cliente debe tener al menos 3 caracteres.')])  # Nombre del cliente que realiza el pedido
    fecha_pedido = models.DateField(null=True, blank=True)  # Fecha en que se realizó el pedido
    producto = models.CharField(max_length=100, validators=[MinLengthValidator(3, message='El nombre del producto debe tener al menos 3 caracteres.')])  # Nombre del producto pedido
    cantidad = models.IntegerField(validators=[MinValueValidator(1, message='La cantidad debe ser al menos 1.')])  # Cantidad del producto pedido
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='pendiente')  # Estado actual del pedido

    class Meta:
        db_table = 'pedidos'  # Nombre de la tabla en la base de datos

    def __str__(self):
        """
        Método que devuelve una representación en cadena del pedido.
        """
        return f"Pedido de {self.cliente} - {self.producto} ({self.id})"  # Formato de representación del objeto
