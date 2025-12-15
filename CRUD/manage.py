#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Importar el módulo os para interactuar con el sistema operativo
import os
# Importar el módulo sys para acceder a parámetros del sistema y funciones del intérprete
import sys

"""

Script de gestión de Django para el proyecto 'proyecto_pedidos'.

Permite ejecutar comandos administrativos como runserver, makemigrations, etc.

"""

# Definir la función principal que ejecuta las tareas administrativas
def main():
    """Run administrative tasks."""
    # Establecer la variable de entorno DJANGO_SETTINGS_MODULE al módulo de configuración del proyecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_pedidos.settings')
    # Intentar importar la función execute_from_command_line de Django
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si falla la importación, lanzar un error con mensaje explicativo
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Ejecutar los comandos administrativos pasados como argumentos de línea de comandos
    execute_from_command_line(sys.argv)

# Verificar si el script se ejecuta directamente (no importado) y llamar a main()
if __name__ == '__main__':
    main()
