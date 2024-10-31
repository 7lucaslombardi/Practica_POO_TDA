class Rectangulo:

    def __init__(self, base : float, altura : float):

        self.base = base
        self.altura = altura

    def calcular_area_perimetro(self):

        area = self.base * self.altura
        perimetro = 2 * (self.base + self.altura)

        print(f"El area del rectangulo es {area}, y el perimetro {perimetro}")