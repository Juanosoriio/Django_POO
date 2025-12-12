import random

class Cuenta:
    def __init__(self,nombre_titular: str,saldo_disponible:float):
        self.__nombre_titular = nombre_titular
        self.__numero_cuenta = abs(random.randint(0, 10**9))
        self.__saldo_disponible = saldo_disponible
        self.estado = True
        
    def inactivar(self):
        if self.estado == False:
            print("La cuenta ya esta inactiva")
        else:
            self.estado = False
        
    def set_ingreso(self, ingreso:float):
        try:
            if ingreso <= 0:
                raise ValueError("El total de ingreso debe ser mayor a cero")
            else:
                self.__saldo_disponible += ingreso
        except (TypeError, ValueError):
            print(f"Error, ingresas un tipo de dato invalido")
                    
    def set_retiro(self, retiro:float):
        try:
            if retiro <= 0:
                raise ValueError("Mano tampoco puede retirar cero o un valor negativo")
            elif retiro > self.__saldo_disponible:
                raise ValueError("Fondos insuficientes para el retiro")
            else: 
                self.__saldo_disponible -= retiro
        except (TypeError):
            print("Mano vuelvase serio y ingrese un numero")
    
    def get_saldo(self) -> str:
        return f"El saldo de la cuenta es: {self.__saldo_disponible}"
    
    @staticmethod
    def transferencia(titular1,titular2,cantidad:float):
        try:
            if cantidad <= 0:
                raise ValueError("Mano no puede transferir un valor de cero o negativo")
            elif cantidad > titular1.__saldo_disponible:
                raise ValueError("Fondos insufiencientes para la transferencia")
            else:
                titular2.__saldo_disponible += cantidad
                titular1.__saldo_disponible -= cantidad
        except(TypeError):
            print("Ingresaste un valor diferente a un numero")
            
    def get_datos_cuenta(self) -> str:
        return f"Titular: {self.__nombre_titular}\n No de cuenta: {self.__numero_cuenta}\n Saldo: {self.__saldo_disponible}"