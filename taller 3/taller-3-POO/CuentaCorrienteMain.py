from CuentaCorriente import Cuenta

def main():
    titular1 = Cuenta("Juan Esteban", 20000)
    titular2 = Cuenta("Carol", 2500)
    
    Cuenta.transferencia(titular1,titular2, 10000)

    print(titular1.get_datos_cuenta())
    print(titular2.get_datos_cuenta())
    
if __name__ == "__main__": #Solo corre este archivo este archivo es el programa principal y no el importado
    main()

# cuenta1 = Cuenta("Juan Esteban", 20000)
# print(cuenta1.set_ingreso("a"))
# print(cuenta1.get_datos_cuenta())


