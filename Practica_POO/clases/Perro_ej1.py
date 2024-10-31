from clases.Animal_ej1 import Animal

class Perro(Animal):

    def __init__(self, nombre : str):
        super().__init__(nombre)

    def realizar_sonido(self):

        sonido = "guau guau"
        print(f"El perro {self.nombre} hace {sonido}")