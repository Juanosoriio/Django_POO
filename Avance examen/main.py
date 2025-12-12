from SistemaClinica import SistemaClinica
from PacienteGeneral import PacienteGeneral
from PacienteUrgencias import PacienteUrgencias
from PacienteUCI import PacienteUCI

def main():
    sistema = SistemaClinica()  # Instancia el sistema de la clínica

    # Crear instancias de diferentes tipos de pacientes
    general = PacienteGeneral("Juan Perez", "12345678", 150000, "Medicina General", 0.20)
    urgencias = PacienteUrgencias("Maria Lopez", "87654321", 200000, 3)
    uci = PacienteUCI("Carlos Gomez", "11223344", 100000, True, 5)

    # Agregar pacientes al sistema
    sistema.agregar_paciente(general)
    sistema.agregar_paciente(urgencias)
    sistema.agregar_paciente(uci)

    # Generar y mostrar el reporte de costos
    sistema.generar_reporte_costos()

if __name__ == "__main__":
    main()
