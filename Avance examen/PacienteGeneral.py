from Paciente import Paciente

# Clase para pacientes de consulta general con descuento EPS
class PacienteGeneral(Paciente):
    def __init__(self, nombre, identificacion, costo_base_servicio, tipo_consulta, descuento_eps, dias_hospitalizacion=0):
        super().__init__(nombre, identificacion, costo_base_servicio, dias_hospitalizacion)
        self.__tipo_consulta = tipo_consulta  # Tipo de consulta (ej: "Medicina General")
        self.__descuento_eps = descuento_eps  # Descuento aplicado por EPS (porcentaje)

    # Propiedades para tipo de consulta y descuento
    @property
    def tipo_consulta(self):
        return self.__tipo_consulta

    @tipo_consulta.setter
    def tipo_consulta(self, value):
        self.__tipo_consulta = value

    @property
    def descuento_eps(self):
        return self.__descuento_eps

    @descuento_eps.setter
    def descuento_eps(self, value):
        self.__descuento_eps = value

    # Calcula costo final aplicando descuento EPS y tasa administrativa
    def calcular_costo_final(self):
        costo_base = self.costo_base_servicio
        descuento = costo_base * self.__descuento_eps
        costo_sin_admin = costo_base - descuento
        return costo_sin_admin + (costo_sin_admin * self.TASA_ADM_CLINICA)

    def __str__(self):
        return f"{super().__str__()}, Tipo: General ({self.__tipo_consulta}), Descuento EPS: {self.__descuento_eps*100}%"