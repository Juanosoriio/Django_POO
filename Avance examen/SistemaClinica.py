from Paciente import Paciente

# Clase controladora que gestiona la lista de pacientes y genera reportes
class SistemaClinica:
    def __init__(self):
        self.lista_pacientes = []  # Lista para almacenar objetos Paciente

    # Agrega un paciente a la lista si es instancia de Paciente
    def agregar_paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self.lista_pacientes.append(paciente)
        else:
            raise ValueError("El objeto debe ser una instancia de Paciente")

    # Genera reporte de costos: muestra cada paciente y totales
    def generar_reporte_costos(self):
        total_facturacion = 0
        total_tasa_admin = 0
        for paciente in self.lista_pacientes:
            costo_final = paciente.calcular_costo_final()
            tasa_admin = paciente.calcular_tasa_administrativa()
            total_facturacion += costo_final
            total_tasa_admin += tasa_admin
            print(f"{paciente}")
        print(f"\nTotal de Facturacion: {total_facturacion:,.0f}")
        print(f"Total de Ingresos por Tasa Administrativa: {total_tasa_admin:,.0f}")