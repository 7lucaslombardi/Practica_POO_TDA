from clases.Animal_ej1 import Animal

class Gato(Animal):

    def __init__(self, nombre : str):
        super().__init__(nombre)

    def mostrar_sonido(self):

        sonido = "miau miau"
        print(f"El gato {self.nombre} hace {sonido}")