# Importar la función path para definir rutas URL
from django.urls import path
# Importar el módulo views de la app actual
from . import views

"""

URLs para la aplicación de pedidos.

"""

# Definición de las rutas URL para las vistas de pedidos
urlpatterns = [
    path('', views.listar_pedidos, name='listar_pedidos'),  # Ruta para listar todos los pedidos
    path('crear/', views.crear_pedido, name='crear_pedido'),  # Ruta para crear un nuevo pedido
    path('<int:pk>/', views.ver_pedido, name='ver_pedido'),  # Ruta para ver un pedido específico por ID
    path('editar/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'),  # Ruta para editar un pedido por ID
    path('eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido'),  # Ruta para eliminar un pedido por ID
]