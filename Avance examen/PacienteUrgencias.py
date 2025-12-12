from Paciente import Paciente

# Clase para pacientes de urgencias con recargo fijo
class PacienteUrgencias(Paciente):
    RECARGO_URGENCIAS = 50000  # Recargo fijo por atención inmediata

    def __init__(self, nombre, identificacion, costo_base_servicio, prioridad, dias_hospitalizacion=0):
        super().__init__(nombre, identificacion, costo_base_servicio, dias_hospitalizacion)
        self.__prioridad = prioridad  # Nivel de prioridad (1-5)

    # Propiedad para prioridad
    @property
    def prioridad(self):
        return self.__prioridad

    @prioridad.setter
    def prioridad(self, value):
        self.__prioridad = value

    # Calcula costo final agregando recargo y tasa administrativa
    def calcular_costo_final(self):
        costo_con_recargo = self.costo_base_servicio + self.RECARGO_URGENCIAS
        return costo_con_recargo + (costo_con_recargo * self.TASA_ADM_CLINICA)

    def __str__(self):
        return f"{super().__str__()}, Tipo: Urgencias, Prioridad: {self.__prioridad}"