'''
Crear un menú de opciones en el main.py que permita
desarrollar las siguientes tareas llamando a funciones
modularizadas en otros archivos.
1- Cargar secuencialmente una lista de alumnos, cada alumno
debe ser un diccionario con cuatro claves: nombre, apellido, edad y
la clave curso que posea de valor una tupla con el curso.
2- Cargar secuencialmente una lista de cursos, cada curso debe
ser un diccionario con dos claves: una tupla que contenga año y
división, debe tener cargada como valor la cantidad de alumnos y
el preceptor a cargo.
3- Generar un set de preceptores para cada año
4- Obtener promedio de edad de un determinado curso.
5- Buscar qué preceptores se encuentran repetidos en dos años distintos.
6- Buscar qué preceptores se encuentran solo en un determinado año.
7- Mostrar nombre y apellido del alumno más jóven y más grande
del colegio.
'''
from funciones.funciones_ejercicio import *


def mostrar_menu():
    print("------------Menú de opciones-------------")
    print("1. Cargar alumnos")
    print("2. Listar alumnos")
    print("3. Cargar cursos")
    print("4. Listar cursos")
    print("5. Salir")

# Bucle principal para mostrar el menú y llamar funciones
while True:
    mostrar_menu()
    
    # Pedir opción al usuario
    opcion = input("Seleccione una opción: ")

    # Ejecutar la función correspondiente
    if opcion == "1":
        cargar_alumnos()
    elif opcion == "2":
        listar_alumnos()
    elif opcion == "3":
        cargar_cursos()
    elif opcion == "4":
        listar_cursos()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
