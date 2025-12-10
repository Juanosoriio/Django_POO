from abc import ABC, abstractmethod

class RecursoDigital(ABC):
    @abstractmethod
    def mostrar_informacion(self):
        pass

    @abstractmethod
    def calcular_costo_descarga(self):
        pass

    @abstractmethod
    def obtener_tipo(self):
        pass

class Material(RecursoDigital):
    def __init__(self, codigo, titulo, precio_base):
        if not self.validar_codigo(codigo):
            raise ValueError("Código no puede estar vacío")
        if not self.validar_precio(precio_base):
            raise ValueError("Precio base no puede ser negativo")
        self.codigo = codigo
        self.titulo = titulo
        self.precio_base = precio_base

    @staticmethod
    def validar_codigo(codigo):
        return bool(codigo.strip())

    @staticmethod
    def validar_precio(precio):
        return precio >= 0

    def __str__(self):
        return f"{self.codigo} – {self.titulo} (${self.precio_base})"

    # Los métodos abstractos se implementarán en las subclases