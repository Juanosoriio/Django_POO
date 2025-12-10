from Paciente import Paciente

# Clase para pacientes en UCI con costo por día de hospitalización
class PacienteUCI(Paciente):
    COSTO_DIA_UCI = 800000  # Costo diario en UCI

    def __init__(self, nombre, identificacion, costo_base_servicio, soporte_vital, dias_hospitalizacion):
        super().__init__(nombre, identificacion, costo_base_servicio, dias_hospitalizacion)
        self.__soporte_vital = soporte_vital  # Indica si requiere soporte vital avanzado

    # Propiedad para soporte vital
    @property
    def soporte_vital(self):
        return self.__soporte_vital

    @soporte_vital.setter
    def soporte_vital(self, value):
        self.__soporte_vital = value

    # Calcula costo final sumando costo base, días en UCI y tasa administrativa
    def calcular_costo_final(self):
        costo_tratamiento = self.costo_base_servicio + (self.dias_hospitalizacion * self.COSTO_DIA_UCI)
        return costo_tratamiento + (costo_tratamiento * self.TASA_ADM_CLINICA)

    def __str__(self):
        soporte = "Si" if self.__soporte_vital else "No"
        return f"{super().__str__()}, Tipo: UCI, Soporte Vital: {soporte}, Dias: {self.dias_hospitalizacion}"