'''
1-Clase para representar un Libro
Crear una clase Libro que tenga las características título, autor y año de publicación. Del
libro se debe poder obtener información, mostrando por mensaje todos sus datos. Se debe
crear la clase e implementarla
'''

from clases.Libro import Libro
from clases.Rectangulo import Rectangulo
from clases.Calculadora import Calculadora
from clases.Perro_ej1 import Perro
from clases.Gato_ej1 import Gato
from clases.Cuenta_bancaria import CuentaBancaria

libro_1 = Libro("Historias", "Picasso", 1984)
libro_2 = Libro("Duendes", "Rolon", 1997)
libro_3 = Libro("Divan", "Martino", 1981)

libro_1.retornar_datos()
libro_2.retornar_datos()
libro_3.retornar_datos()


'''
2- Clase para representar un Rectángulo 
Crear una clase rectángulo que tenga las características base y altura. 
Del rectángulo se debe poder calcular el área y el perímetro.
Se debe crear la clase e implementarla.
'''
rectangulo_1 = Rectangulo(13, 8.5)
rectangulo_2 = Rectangulo(16.50, 4.5)
rectangulo_3 = Rectangulo(20.60, 12)

rectangulo_1.calcular_area_perimetro()
rectangulo_2.calcular_area_perimetro()
rectangulo_3.calcular_area_perimetro()


'''
3- Clase para representar una Calculadora 
Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división. 
Se debe crear la clase e implementarla.
'''
operacion_1 = Calculadora(20, 10)

operacion_1.sumar()
operacion_1.restar()
operacion_1.multiplicar()
operacion_1.dividir()

'''
4- Herencia de clases
Crear una clase Animal que tenga la característica nombre. 
La clase Perro que herede de Animal las características y realice el sonido “guau guau”. 
La clase Gato que herede de Animal las características y realice el sonido “Miau”. 
Del gato y el perro se debe poder mostrar el sonido que realizan. 
Se debe crear la clase e implementarla.
'''

animal_1 = Perro("Pedrito")
animal_2 = Gato("Josecito")

animal_1.realizar_sonido()
animal_2.mostrar_sonido()

'''
5- Encapsulamiento 
Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado. 
De la cuenta bancaria se puede obtener el saldo, depositar o retirar (en
cada caso imprimir que fue exitoso). 
Se debe crear la clase e implementarla.
'''

cuenta_1 = CuentaBancaria("Jose", 2000)

cuenta_1.obtener_saldo()
cuenta_1.depositar(1000)
cuenta_1.retirar(500)