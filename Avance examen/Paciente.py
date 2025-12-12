from abc import ABC, abstractmethod

# Clase base abstracta para todos los tipos de pacientes
class Paciente(ABC):
    TASA_ADM_CLINICA = 0.05  # Tasa administrativa fija del 5%

    def __init__(self, nombre, identificacion, costo_base_servicio, dias_hospitalizacion=0):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__costo_base_servicio = costo_base_servicio
        self._dias_hospitalizacion = dias_hospitalizacion

    # Propiedades para acceder y modificar atributos encapsulados
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, value):
        self.__identificacion = value

    @property
    def costo_base_servicio(self):
        return self.__costo_base_servicio

    @costo_base_servicio.setter
    def costo_base_servicio(self, value):
        self.__costo_base_servicio = value

    @property
    def dias_hospitalizacion(self):
        return self._dias_hospitalizacion

    @dias_hospitalizacion.setter
    def dias_hospitalizacion(self, value):
        self._dias_hospitalizacion = value

    # Método abstracto que cada subclase debe implementar para calcular el costo final
    @abstractmethod
    def calcular_costo_final(self):
        pass

    # Calcula la tasa administrativa sobre el costo final
    def calcular_tasa_administrativa(self):
        return self.calcular_costo_final() * self.TASA_ADM_CLINICA

    # Representación en string del paciente
    def __str__(self):
        return f"Paciente: {self.__nombre}, ID: {self.__identificacion}, Costo Final: {self.calcular_costo_final():,.0f}"


        # Ayuda a mejorar la legibilidad del código y asegura que cada tipo de paciente implemente su propia lógica para calcular el costo final.