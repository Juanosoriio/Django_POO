from lavadora_estandar import LavadoraEstandar
from lavadora_inteligente import LavadoraInteligente

class SistemaLavaSmart:
    def __init__(self):
        self.clientes_atendidos = []
        self.total_iva = 0
        self.total_ganancia = 0
        self.total_facturado = 0

    def crear_lavadora(self, tipo, kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato):
        if tipo.lower() == 'estandar':
            return LavadoraEstandar(kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato)
        elif tipo.lower() == 'inteligente':
            return LavadoraInteligente(kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato)
        else:
            raise ValueError("Tipo de lavadora no válido.")

    def ejecutar_ciclo(self, lavadora, nombre_cliente):
        try:
            lavadora.encender()
            lavadora._validar_kilos()
            print(f"Cliente: {nombre_cliente}")
            print(f"Kilos: {lavadora._kilos}")
            print(f"Tipo de ropa: {', '.join(lavadora._tipo_ropa)}")
            costos = lavadora._calcular_costos()
            energia = lavadora._calcular_consumo_energia()
            print(f"Costo por kilo: ${lavadora._precio_kilo}")
            print(f"Costo total estimado: ${costos['costo_iva'] + energia['costo_energia']:.2f}")
            lavadora._llenar()
            if isinstance(lavadora, LavadoraInteligente):
                lavadora.detectar_tipo_ropa()
                lavadora.conectar_wifi()
            lavadora.lavar()
            lavadora._enjuagar()
            while True:
                opcion_secar = input("¿Desea secar? (s/n): ").strip().lower()
                if opcion_secar in ['s', 'n']:
                    secar = opcion_secar == 's'
                    break
                print("Opción inválida. Ingrese 's' para sí o 'n' para no.")
            if secar:
                lavadora._secar()
            lavadora.ciclo_terminado()
            # Registrar para el dueño
            self.clientes_atendidos.append({
                'nombre': nombre_cliente,
                'kilos': lavadora._kilos,
                'tipo_ropa': lavadora._tipo_ropa,
                'tipo_lavadora': type(lavadora).__name__,
                'iva': costos['costo_iva'] - costos['costo_aumentado'],
                'ganancia': costos['utilidad'],
                'facturado': costos['costo_iva'] + energia['costo_energia']
            })
            self.total_iva += costos['costo_iva'] - costos['costo_aumentado']
            self.total_ganancia += costos['utilidad']
            self.total_facturado += costos['costo_iva'] + energia['costo_energia']
        except ValueError as e:
            print(f"Error: {e}")

    def mostrar_reporte_dueno(self):
        print("\n--- REPORTE PARA EL DUEÑO ---")
        print(f"Total de clientes atendidos: {len(self.clientes_atendidos)}")
        print(f"IVA total cobrado: ${self.total_iva:.2f}")
        print(f"Ganancia neta total (30%): ${self.total_ganancia:.2f}")
        print(f"Total facturado: ${self.total_facturado:.2f}")
        for cliente in self.clientes_atendidos:
            print(f"Cliente: {cliente['nombre']}, Facturado: ${cliente['facturado']:.2f}")