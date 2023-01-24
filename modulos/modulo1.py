# Esta es la clase módulo1.py, que se encuentra en la carpeta modulos, y lo
# que hace es importar la función dame() de cadenas.py, y la función
# a_mayusc() de cadenas.py.

'''
import cadenas

print('***************************************************')
print('La versión del paquete cadenas es:', cadenas.__version__)
print('')
print('*********************************************************')

cadenas.dame('Saludos')
print('-----------------------------')
cadenas.medio('universidad')
print('-----------------------------')
print(cadenas.a_mayusc2('Soy todo minusculo en enero 2023'))
'''
'''
print('Versión 2 de importar módulos')

from cadenas import dame, medio, a_mayusc2
dame('Prueba')
medio('Cuenca')
'''
'''
print('Versión 3 de importar módulos')
from cadenas import *
dame('Prueba')
medio('Cuenca')
'''

# Vamos a importar modulos de la librería estándar de Python.
'''
print('Versión 1 de importar módulos de la librería estándar de Python')
import calendar
año = int(input('Introduce un año: '))
calendar.prcal(año)
'''
'''
print('Versión 2 de importar módulos de la librería estándar de Python')
import calendar
print('Día de la semana:', calendar.weekday(2023, 1, 24))
'''
'''
print('Versión 3 de importar módulos de la librería estándar de Python')
import calendar
dias = {0: 'Lunes', 1: 'Martes', 2: 'Miercoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}
print('Día de la semana:', dias[calendar.weekday(2023, 1, 24)])
'''
'''
# Vamos a hacer un programa que nos diga si un año es bisiesto o no.
# Como la función isleap() devuelve True o False, podemos usarla en un if 
# directamente y así nos dirá si es bisiesto o no.
print('Versión 4 de importar módulos de la librería estándar de Python')
import calendar
anio = int(input('Introduce un año: '))
if (calendar.isleap(anio) == True):
    print('El año', anio, 'es bisiesto')
else:
    print('El año', anio, 'no es bisiesto')
'''











