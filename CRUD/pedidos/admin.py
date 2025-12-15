# Importar el módulo admin de Django
from django.contrib import admin
# Importar el modelo Pedido desde el módulo actual
from .models import Pedido

# Registrar tus modelos aquí.

"""

Configuración del administrador para la aplicación de pedidos.

"""

# Registrar el modelo Pedido en el sitio de administración de Django
admin.site.register(Pedido)
