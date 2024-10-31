class Calculadora:

    def __init__(self, num_1 : int, num_2 : int):
        
        self.num_1 = num_1
        self.num_2 = num_2

    def sumar(self):

        print(f"La suma de ambos numeros es {self.num_1 + self.num_2}")

    def restar(self):

        print(f"La resta de ambos numeros es {self.num_1 - self.num_2}")

    def multiplicar(self):

        print(f"La multiplicacion de ambos numeros es {self.num_1 * self.num_2}")

    def dividir(self):

        print(f"La division de ambos numeros es {self.num_1 / self.num_2}")
