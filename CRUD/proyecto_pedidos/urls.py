"""proyecto_pedidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importar el sitio de administración de Django
from django.contrib import admin
# Importar funciones para definir rutas URL
from django.urls import path, include
# Importar la función redirect para redirecciones
from django.shortcuts import redirect


# Definición de las rutas principales del proyecto
urlpatterns = [
    # Redirección automática desde la raíz ("") hacia la vista listar_pedidos
    path('', lambda request: redirect('listar_pedidos')),  # 👈 Redirección automática
    # Ruta que enlaza la URL /admin/ con el administrador interno de Django
    path("admin/", admin.site.urls),
    # Inclusión de las rutas del módulo "pedidos" bajo el prefijo /pedidos/
    path("pedidos/", include("pedidos.urls")),
]
