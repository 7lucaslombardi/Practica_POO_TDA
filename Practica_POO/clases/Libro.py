class Libro:

    def __init__(self, titulo : str, autor : str , año : int):
        
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def retornar_datos(self):

        print(f"El titulo del libro es {self.titulo}, su autor es {self.autor} ,y se publico en el año {self.año} ")