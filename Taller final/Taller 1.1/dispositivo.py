from abc import ABC, abstractmethod

# INTERFAZ / CONTRATO
class IDispositivo(ABC):
    """Interfaz que obliga a implementar ciertos métodos."""
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def aplicar_descuento(self, porcentaje):
        pass

    @abstractmethod
    def obtener_info(self):
        pass

# ======================================
# UTILIDAD CON MÉTODOS ESTÁTICOS
# ======================================
class Validador:
    """Utilidades comunes para validar datos."""
    @staticmethod
    def validar_precio(precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

    @staticmethod
    def validar_codigo(codigo):
        if len(codigo) < 4:
            raise ValueError("El código debe tener al menos 4 caracteres.")

# ======================================
# CLASE ABSTRACTA (CLASE VIRTUAL)
# ======================================
class Dispositivo(IDispositivo):
    """Clase base que actúa como clase abstracta y virtual."""
    def __init__(self, codigo, marca, precio):
        Validador.validar_codigo(codigo)
        Validador.validar_precio(precio)
        self._codigo = codigo
        self._marca = marca
        self._precio = precio

    def aplicar_descuento(self, porcentaje):
        self._precio -= self._precio * porcentaje

    def __str__(self):
        """Método mágico para representar el dispositivo."""
        return f"{self._codigo} - {self._marca} (${self._precio:,.0f})"