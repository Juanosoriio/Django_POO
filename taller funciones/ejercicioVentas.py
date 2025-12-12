#importar modulos
from datetime import date, datetime
import time

#Definir variables

ventas_medellin = float(input("Ingrese las ventas de Medellin: "))
ventas_cali = float(input("Ingrese las ventas de Cali: "))
ventas_bogota = float(input("Ingrese las ventas de Bogota: "))

valor_mayor = max(ventas_bogota,ventas_cali,ventas_medellin)
valor_minimo = min(ventas_bogota,ventas_cali,ventas_medellin)

#Creación de las variables de fechas

fecha_actual_forma1 = date.today()
fecha_actual_forma2 = date.today()
fecha_actual_forma3 = datetime.now()

#Impresión de las variables

print(f"La fecha forma 1 es: {fecha_actual_forma1}")
print(f"La fecha forma 2 es: {fecha_actual_forma2.strftime("%d/%m/%y")}") #función para indicar al sistema como mostrar la fecha
print(f"La fecha forma 3 es: {fecha_actual_forma3}")

#Calcular las ventas totales y promedio
#Imprimir resultados

time.sleep(3)

ventas_total = ventas_bogota+ventas_cali+ventas_medellin
promedio_ventas = ventas_total/3

print("\n === Resumen de ventas ===")
print(f"La fecha hora actual es: {fecha_actual_forma1}, forma 1: Medellin vendio ${ventas_medellin:.2f}, forma 2: Medellin vendio ${ventas_medellin:,.2f}")
print(f"La fecha hora actual es: {fecha_actual_forma1}, forma 1: cali vendio ${ventas_cali:.2f}, forma 2: cali vendio ${ventas_cali:,.2f}")
print(f"La fecha hora actual es: {fecha_actual_forma1}, forma 1: bogota vendio ${ventas_bogota:.2f}, forma 2: bogota vendio ${ventas_bogota:,.2f}")
print(f"=== Resumen de ventas === \nTotal ventas = ${ventas_total}. \nPromedio = ${promedio_ventas}")

# print(f"Total ventas = {ventas_total}.\n === Resumen de ventas ===  \nPromedio = {promedio_ventas}")
# print(f"La venta mas grande es: {valor_mayor}")
# print(f"La venta mas pequeño es: {valor_minimo}")