# a. Función sin parametros ni retorno
# ============
def sin_parametros():
    print("Hola mundo")

sin_parametros()

# b. Función con parametros pero sin retorno
# ============
def con_parametros(nombre):
    print(f"Hola {nombre}")
    
con_parametros("Juan")

# c. Función calcular Iva con parametro y iva del 19
# =================
def calcular_iva(valor):
    return valor * 0.19

print(calcular_iva(100))

# d. Función que calcule el valor del iva de una compra 
#   - Se debe solicitar al usuario el subtotal (antes de impuestos) 
#   - Iva del 19% 
#   - Retornar el valor del iva correspondiente
    # ==================
def iva_subtotal(subtotal):
    impuesto = subtotal * 0.19
    return  impuesto

subtotal = float(input("Ingrese el subtotal de la compra: "))

print(f"El impuesto del subtotal ingresado {subtotal} es: {iva_subtotal(subtotal)}")

# def iva_subtotal():
#     while True:
#         try:
#             global subtotal
#             subtotal = float(input("Ingrese el subtotal de la compra: "))
#             impuesto = subtotal * 0.19
#             return  impuesto
#             break
#         except:
#             print("Ingreso un dato invalido por favor intentelo de nuevo")
# valor = iva_subtotal()
# print(f"El impuesto del subtotal ingresado {subtotal} es: {valor}")

# def iva_subtotal():
#             global subtotal
#             subtotal = float(input("Ingrese el subtotal de la compra: "))
#             impuesto = subtotal * 0.19
#             return  impuesto
# valor = iva_subtotal()
# print(f"El impuesto del subtotal ingresado {subtotal} es: {valor}")

# e. Calcular ventas con varios parametros y retorno
#   - la función se debe llamar calcular_total
#   - la función debe recibir dos parametros
#       - subtotal e iva
#   - debe sumar el iva y el total a pagar
#   - mostrar en pasntalal el total calculado usando f string
# ==================
def calcular_total(subtotal_2,iva):
    total = subtotal_2+(subtotal_2 * iva)/100
    return total

subtotal = float(input("Ingrese el segundo subtotal de la compra: "))
iva = float(input("Ingrese el iva: "))

print(f"El subtotal fue {subtotal}, con un impuesto del {iva}%, el total a pagar es de: {calcular_total(subtotal,iva)}")

# Retos iniciales

# Desarrollar una función que reciba tres números y devuelva la suma de ellos.
# ===========================                 
def suma(num1,num2,num3):
    return num1+num2+num3

print(f"La suma de los numeros es {suma(1,2,3)}")

# Desarrollar una función que reciba tres números ingresados por el cliente y devuelva la suma de ellos. 
# =================================
def suma_ingresados(num1,num2,num3):
    return num1+num2+num3

num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))
num3 = float(input("Ingrese numero 3: "))

print(f"La suma de los numeros ingresados es: {suma_ingresados(num1,num2,num3)}")

# Desarrollar una función en Python que recibe los gastos de pasajes de los 6 días de la semana y calcular el 
# total gastado. 

def calcular_pasajes(pasaje_1,pasaje_2,pasaje_3,pasaje_4,pasaje_5,pasaje_6):
    return pasaje_1+pasaje_2+pasaje_3+pasaje_4+pasaje_5+pasaje_6

pasaje_1 = float(input("Ingrese el pasaje 1: "))
pasaje_2 = float(input("Ingrese el pasaje 2: "))
pasaje_3 = float(input("Ingrese el pasaje 3: "))
pasaje_4 = float(input("Ingrese el pasaje 4: "))
pasaje_5 = float(input("Ingrese el pasaje 5: "))
pasaje_6 = float(input("Ingrese el pasaje 6: "))

print(f"El total gastado en pasajes de la semana es de: {calcular_pasajes(pasaje_1,pasaje_2,pasaje_3,pasaje_4,pasaje_5,pasaje_6)}")

def calcular_pasajes(pasaje, contador):
    return contador+pasaje

contador = 0
for i in range(1,7):
    pasaje = float(input(f"ingrese el pasaje del dia {i}: "))
    contador = calcular_pasajes(pasaje,contador)

print(f"El total gastado en la semana es de: {contador}")

#Crear una función que toma el precio unitario, la cantidad vendida y devuelve el total de la venta.

def total_venta(precio,cantidad):
    return precio+cantidad

print(f"El total de la venta es de: {total_venta(1500,6)}")

#Crear una función que tome el costo unitario, el precio de venta y devuelve la ganancia obtenida.

def total_ganancia(precio,cantidad):
    return precio+cantidad

print(f"El total de la ganancia obtenida es de: {total_ganancia(1500,6)}")

#función en Python que calcula el total a pagar de una nómina, dado el valor por hora, la cantidad de horas 
# trabajadas, las deducciones de fondo de empleados, otras deducciones, mientras el empleado esté activo:

def total_nomina(valor_hora,cantidad_hora,deducciones,otras):
    total_deducciones = deducciones+otras
    total_pagar = (valor_hora*cantidad_hora)-total_deducciones
    return total_pagar

activo = input("El empleado esta activo? si / no ").lower()

if activo == "si":
    valor_hora = float(input("Ingrese el valor hora: "))
    cantidad_hora = int(input("Ingrese la cantidad de horas trabajas: "))
    deducciones = float(input("Ingrese las deducciones del fondo de empleados: "))
    otras_deducciones = float(input("Ingrese otras deducciones: "))
    print(f"El total a pagar en nomina es de: {total_nomina(valor_hora,cantidad_hora,deducciones,otras_deducciones)}")
else:
    print("El empleado no esta activo")


#Crear una función que tome el precio original y el porcentaje de descuento y devuelve el precio con descuento.

def descuento(precio_original,porcentaje_descuento):
    descuento_total = (precio_original*porcentaje_descuento)/100 
    return precio_original-descuento_total

print(f"El valor del producto con descuento es de {descuento(1000,10)}")

#Desarrolle una función que calcule el saldo final del inventario teniendo en cuenta esta recibe 4 
# parámetros y que saldo final inventario= Saldo inicialmes + cantidadesCompradas- cantidades vendidas y 
# cantDadaDeBaja.

def calcular_saldo_final(saldo_inicial, cantidad_comprada, cantidad_vendida, cantidad_dada_baja):
    saldo_final = saldo_inicial + cantidad_comprada - (cantidad_vendida + cantidad_dada_baja)
    return saldo_final

saldo_inicial = float(input("Ingrese el saldo inicial del mes: "))
cantidad_comprada = float(input("Ingrese la cantidad comprada: "))
cantidad_vendida = float(input("Ingrese la cantidad vendida: "))
cantidad_dada_baja = float(input("Ingrese la cantidad dada de baja: "))

saldo_final = calcular_saldo_final(saldo_inicial, cantidad_comprada, cantidad_vendida, cantidad_dada_baja)
print(f"El saldo final del inventario es: {saldo_final}") 

def calcular (subtotal):
    return subtotal * 0.19

print(f"La suma de los valores es: {calcular(float(input("Ingrese un subtotal: ")))}")
