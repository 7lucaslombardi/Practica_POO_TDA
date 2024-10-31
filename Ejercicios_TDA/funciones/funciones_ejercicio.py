
lista_alumnos = []

def cargar_alumnos():
    
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos que desea cargar: "))
    for i in range(cantidad_alumnos):
        print(f"Ingresando datos del alumno {i + 1}:")

        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        curso = input("Ingrese el curso del alumno: ")

        # Crear el diccionario del alumno
        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "curso": (curso)
        }

        # Agregar el alumno a la lista
        lista_alumnos.append(alumno)
        print("Alumno agregado")

def listar_alumnos():
    print("Lista de alumnos:")
    for alumno in lista_alumnos:
        print(alumno)

# Lista para almacenar los cursos
lista_cursos = []

def cargar_cursos():
    cantidad_cursos = int(input("Ingrese la cantidad de cursos que desea cargar: "))
    
    for i in range(cantidad_cursos):
        print(f"Ingresando datos del curso {i + 1}:")

        # Ingreso del año y la división como tupla
        año = input("Ingrese el año del curso: ")
        division = input("Ingrese la división del curso: ")
        
        # Ingreso de la cantidad de alumnos y validar que sea un número
        cantidad_alumnos_valida = True
        while cantidad_alumnos_valida:
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
            cantidad_alumnos_valida = False

        # Ingreso del preceptor a cargo
        preceptor = input("Ingrese el nombre del preceptor a cargo: ")

        # Crear el diccionario del curso
        curso = { (año, division): 
                {"cantidad_alumnos": cantidad_alumnos,
                "preceptor": preceptor} }

        # Agregar el curso a la lista
        lista_cursos.append(curso)
        print("Curso agregado con éxito")

def listar_cursos():
    print("Lista de cursos:")
    for curso in lista_cursos:
        print(curso)

def generar_set_preceptores():
    preceptores_por_año = {}

    
