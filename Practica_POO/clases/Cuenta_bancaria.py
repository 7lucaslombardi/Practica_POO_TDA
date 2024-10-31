class CuentaBancaria:
    
    def __init__(self, titular : str, saldo : float):
        
        self.__titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):

        print(f"Saldo inicial: {self.__saldo}")

    def depositar(self, cantidad : float):

        if cantidad > 0:
            self.__saldo += cantidad
            print("Deposito exitoso")
            print(f"Saldo actual {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0")


    def retirar(self, cantidad : float):

        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro exitoso")
            print(f"Saldo actual {self.__saldo}")
        elif cantidad > self.__saldo:
            print("Saldo insuficiente para retitar")
        else:
            print("La cantidad para retirar debe ser mayor a 0")