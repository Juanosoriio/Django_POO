# Importar el módulo forms de Django para crear formularios
from django import forms
# Importar el modelo Pedido para el formulario
from pedidos.models import Pedido

"""

Formularios para el proyecto de pedidos.

"""

class PedidoForm(forms.ModelForm):
    """
    Formulario basado en el modelo Pedido para crear y editar pedidos.
    """

    class Meta:
        model = Pedido  # Modelo en el que se basa el formulario
        fields = ['cliente', 'fecha_pedido', 'producto', 'cantidad', 'estado']  # Campos a incluir en el formulario
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={'type': 'date'}),  # Widget para fecha con input de tipo date
            'cliente': forms.TextInput(attrs={'minlength': '3'}),  # Campo de texto con longitud mínima
            'producto': forms.TextInput(attrs={'minlength': '3'}),  # Campo de texto con longitud mínima
            'cantidad': forms.NumberInput(attrs={'min': '1'}),  # Campo numérico con mínimo 1
        }

