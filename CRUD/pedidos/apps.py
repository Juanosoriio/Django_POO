# Importar AppConfig de Django para configurar aplicaciones
from django.apps import AppConfig


class PedidosConfig(AppConfig):
    """
    Configuración de la aplicación 'pedidos'.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Campo auto por defecto para claves primarias
    name = 'pedidos'  # Nombre de la aplicación
