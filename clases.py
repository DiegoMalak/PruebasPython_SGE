print('************************************************************')
print('CLASES EN PYTHON 1')
'''
print('*************************************************************')
# Ejemplo creación de una clase.
print('CLASES EJEMPLO 1')
class miclase:
    def saludo(self):
        return 'FELIZ ANIO 2023'

x = miclase().saludo() # Creamos un objeto de la clase Miclase y llamamos al método saludo.
y = miclase().saludo() + ' Alumnos dam'

print(x)
print(y)
'''
'''
print('*************************************************************')
print('CLASES EJEMPLO 2')
# Creamos una clase vacía.
class Empleado:
    pass

# Creamos un objeto de la clase Empleado.
javier = Empleado()
# Se rellenan los atributos del objeto javier.
javier.nombre = 'Javier Jimenez'
javier.departamento = 'Laboratorio Informatica'
javier.sueldo = 850

# Imprimimos los atributos del objeto javier.
print(javier.nombre)
print(javier.departamento)
print(javier.sueldo, '€')
'''
'''
print('*************************************************************')
print('CLASES EJEMPLO 3')


class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.deportes = []

    def add_deporte(self, deporte):
        self.deportes.append(deporte)

a1 = Alumno('Javier')
a2 = Alumno('Paula')
a3 = Alumno('Carlos')

a1.add_deporte('fútbol')
a1.add_deporte('tenis')
a2.add_deporte('natación')
a2.add_deporte('atletismo')
a3.add_deporte('voleibol')
a3.add_deporte('tenis')

# Imprimimos los atributos del objeto javier.
print(a1.nombre)
print(a1.deportes)
print(a2.deportes)
print(a3.deportes)
print(Alumno('Diego').nombre)
print(Alumno('Diego').deportes)
'''
'''
print('*************************************************************')
print('CLASES EJEMPLO 4')
# Función definida fuera de la clase. Calculamos el área de un rectángulo.
def area(self, base, altura):
    s = base * altura
    return s

class Figura:
    def __init__(self, nombre): # Constructor de la clase.
        self.nombre = nombre # Atributo nombre.

    spfc = area # Atributo spfc que es una función. (spfc = superficie de la figura)

    def mensaje(self): # Método mensaje, que devuelve un mensaje.
        return 'Se va a calcular el área de la figura:' # Se puede asignar una función a un atributo dentro de la clase.
    h = mensaje # Se puede asignar una función a una variable dentro de la clase.

# Creamos un objeto de la clase Figura.
obj1 = Figura('Rectángulo')
# Imprimimos el atributo nombre del objeto obj1.
print(obj1.h()), print(obj1.nombre)
# Imprimimos el atributo spfc del objeto obj1.
print(obj1.spfc(2, 5), "cm2")
'''

print('*************************************************************')
print('CLASES EJEMPLO 5')
# Los métodos de la clase pueden llamar a otros métodos de la
# misma clase mediante atributos del método self.
class Articulos:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add2veces(self, x):
        self.add(x)
        self.add(x)

# Creamos un objeto de la clase Articulos.
compra1 = Articulos()
compra1.add('Leche')
compra1.add('Pan')
compra1.add2veces('Vino')

# Imprimimos el atributo data del objeto compra1.
print(compra1.data)


print('*************************************************************')
print('CLASES EJEMPLO 6')
# Herencia simple y múltiple.

print('')

class Palabras(Articulos): # Herencia simple.
    def __init__(self): # Constructor de la clase.
        self.data = [] # Atributo data.

    def Mayusc(self, palabra): # Método Mayusc.
        self.palabra = palabra # Atributo palabra.
        print(palabra.upper()) # Imprimimos la palabra en mayúsculas.

frase1 = Palabras() # Creamos un objeto de la clase Palabras.
frase1.Mayusc('todo está en minúsculas') # Llamamos al método Mayusc.
frase1.add('HOLA') # Llamamos al método add de la clase Articulos.
frase1.add('FELIZ ANIO 2023') # Llamamos al método add de la clase Articulos.
frase1.add2veces('adios') # Llamamos al método add2veces de la clase Articulos.

print(frase1.data) # Imprimimos el atributo data del objeto frase1.
print()


print('*************************************************************')
print('CLASES EJEMPLO 7')
print('')
# Herencia múltiple.

class Adjuntar(): # Herencia simple.
    def __init__(self): # Constructor de la clase.
        self.data = [] # Atributo data.

    def adjuntarTexto(self, palabra): # Método adjuntarTexto.
        palabra = palabra + 'TEXTOADJUNTO' # Atributo palabra.
        print(palabra) # Imprimimos la palabra.

palabra1 = Adjuntar() # Creamos un objeto de la clase Adjuntar.
palabra1.adjuntarTexto('hhhh') # Llamamos al método adjuntarTexto para adjuntar texto a la palabra.
print()

print('*************************************************************')
print('CLASES EJEMPLO 8')
print('')
class Texto(Palabras, Adjuntar):
    def __init__(self):
        self.data = []

    def longitud(self, text):
        print(len(text))

f1 = Texto()
f1.Mayusc('no es mayúscula')        # Herencia simple, método de la clase Palabras.
f1.adjuntarTexto('CicloFormativo')  # Herencia simple, método de la clase Adjuntar.
f1.longitud('CampusVirtual')        # Herencia múltiple, método de la clase Texto.
f1.add('PRUEBAADD')                 # Herencia simple, método de la clase Articulos.

print(f1.data) # Imprimimos el atributo data del objeto f1.
print()