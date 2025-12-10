from sistema_lava_smart import SistemaLavaSmart

def main():
    sistema = SistemaLavaSmart()
    while True:
        print("\n--- Sistema Lava Smart ---")
        while True:
            nombre = input("Nombre del cliente (o 'salir' para terminar): ").strip()
            if nombre.lower() == 'salir':
                sistema.mostrar_reporte_dueno()
                return
            if nombre and len(nombre) >= 2:
                break
            print("El nombre debe tener al menos 2 caracteres y no puede estar vacío. Intente de nuevo.")

        while True:
            try:
                kilos = float(input("Kilos de ropa (5-45): "))
                if 5 <= kilos <= 45:
                    break
                else:
                    print("Los kilos deben estar entre 5 y 45. Intente de nuevo.")
            except ValueError:
                print("Ingrese un número válido para kilos. Intente de nuevo.")

        tipos_permitidos = ['zapatos', 'pantalon', 'vestidos', 'camisas']
        print(f"Tipos de ropa permitidos: {', '.join(tipos_permitidos)}")
        while True:
            tipo_ropa_input = input("Tipo de ropa (separados por coma): ").strip()
            tipo_ropa = [t.strip().lower() for t in tipo_ropa_input.split(',') if t.strip()]
            if tipo_ropa:
                valido = True
                for t in tipo_ropa:
                    if t not in tipos_permitidos:
                        valido = False
                        break
                if valido:
                    break
                else:
                    print("Solo se permiten los tipos: zapatos, pantalon, vestidos, camisas. Intente de nuevo.")
            else:
                print("Debe ingresar al menos un tipo de ropa. Intente de nuevo.")

        while True:
            tipo_lavadora = input("Tipo de lavadora (estandar/inteligente): ").strip().lower()
            if tipo_lavadora in ['estandar', 'inteligente']:
                break
            print("Tipo de lavadora debe ser 'estandar' o 'inteligente'. Intente de nuevo.")

        while True:
            try:
                tiempo_lavado = int(input("Tiempo de lavado en minutos (1-60): "))
                if 1 <= tiempo_lavado <= 60:
                    break
                else:
                    print("El tiempo de lavado debe estar entre 1 y 60 minutos. Intente de nuevo.")
            except ValueError:
                print("Ingrese un número entero válido para tiempo de lavado. Intente de nuevo.")

        while True:
            try:
                potencia_kw = float(input("Potencia en kW: "))
                if potencia_kw > 0:
                    break
                else:
                    print("La potencia debe ser un número positivo. Intente de nuevo.")
            except ValueError:
                print("Ingrese un número válido para potencia. Intente de nuevo.")

        while True:
            try:
                estrato = int(input("Estrato (2-5): "))
                if 2 <= estrato <= 5:
                    break
                else:
                    print("El estrato debe estar entre 2 y 5. Intente de nuevo.")
            except ValueError:
                print("Ingrese un número entero válido para estrato. Intente de nuevo.")

        try:
            lavadora = sistema.crear_lavadora(tipo_lavadora, kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato)
            sistema.ejecutar_ciclo(lavadora, nombre)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()