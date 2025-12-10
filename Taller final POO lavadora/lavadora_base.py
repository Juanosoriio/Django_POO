import time
import winsound
from datetime import datetime

class LavadoraBase:
    def __init__(self, kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato):
        self._kilos = kilos
        self._tipo_ropa = tipo_ropa if isinstance(tipo_ropa, list) else [tipo_ropa]
        self.__estado = False  # privado: apagada inicialmente
        self._tiempo_lavado = tiempo_lavado
        self._precio_kilo = 10000
        self._aumento_especial = 0.05
        self._iva = 0.19
        self._potencia_kw = potencia_kw
        self._estrato = estrato

    def encender(self):
        if not self.__estado:
            self.__estado = True
            winsound.PlaySound('sonidos/sonido-encendido.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            print("🔊 Sonido de encendido reproducido. Lavadora encendida.")
        else:
            print("La lavadora ya está encendida.")

    def _validar_kilos(self):
        if not (5 <= self._kilos <= 45):
            raise ValueError("Los kilos deben estar entre 5 y 45 kg.")

    def _llenar(self):
        winsound.PlaySound('sonidos/llenar.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        print("Llenando la lavadora...")
        time.sleep(7)  # Simula 7 segundos
        print("Lavadora llena.")

    def lavar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas.")

    def _enjuagar(self):
        winsound.PlaySound('sonidos/enjuagar.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        print("Enjuagando...")

    def _secar(self):
        winsound.PlaySound('sonidos/secar.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        print("Secando...")

    def ciclo_terminado(self):
        winsound.PlaySound('sonidos/secar.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        print("🔊 Sonido de finalización reproducido. Ciclo completado.")
        self._mostrar_reporte_cliente()

    def _calcular_costos(self):
        costo_base = self._kilos * self._precio_kilo
        prendas_especiales = ['interior', 'pijamas', 'vestidos']
        aumento = 0
        if any(prenda.lower() in prendas_especiales for prenda in self._tipo_ropa):
            aumento = costo_base * self._aumento_especial
        costo_aumentado = costo_base + aumento
        costo_iva = costo_aumentado * (1 + self._iva)
        utilidad = costo_aumentado * 0.30
        return {
            'costo_base': costo_base,
            'aumento': aumento,
            'costo_aumentado': costo_aumentado,
            'costo_iva': costo_iva,
            'utilidad': utilidad
        }

    def _calcular_consumo_energia(self):
        kwh_operacion = self._potencia_kw * (self._tiempo_lavado / 60)
        tarifas = {2: 867.8, 3: 737.6, 4: 867.8, 5: 1041}
        tarifa = tarifas.get(self._estrato, 867.8)  # default estrato 4
        costo_energia = kwh_operacion * tarifa
        return {
            'kwh': kwh_operacion,
            'costo_energia': costo_energia
        }

    def _mostrar_reporte_cliente(self):
        costos = self._calcular_costos()
        energia = self._calcular_consumo_energia()
        print("\n--- REPORTE DEL CLIENTE ---")
        print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Kilos lavados: {self._kilos}")
        print(f"Tipo de prenda: {', '.join(self._tipo_ropa)}")
        print(f"Costo por kilo: ${self._precio_kilo}")
        print(f"Costo total sin IVA: ${costos['costo_base']}")
        print(f"Aumento especial (5%): ${costos['aumento']}")
        print(f"Costo total con IVA: ${costos['costo_iva']}")
        print(f"Consumo de energía: {energia['kwh']:.2f} kWh")
        print(f"Costo energético: ${energia['costo_energia']:.2f}")
        print(f"Total a pagar: ${costos['costo_iva'] + energia['costo_energia']:.2f}")
        print("Gracias por usar Lava Smart")