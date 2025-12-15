"""

Inicialización del paquete proyecto_pedidos.

Configura pymysql para ser usado como mysqlclient en Django.

"""

# Importar pymysql para conectarse a MySQL
import pymysql

# Hack para que Django acepte pymysql como si fuera mysqlclient
pymysql.version_info = (2, 2, 1, "final", 0)  # Establecer información de versión falsa
pymysql.install_as_MySQLdb()  # Instalar pymysql como MySQLdb