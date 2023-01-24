print('')
print('**********************************************************************')
print('INTRODUCCIÓN')
print('LECTURA Y ESCRITURA DE ARCHIVOS')

'''
r -> read
r+ -> read and write
w -> Sobre-escribe el archivo
a -> Añade al final del archivo
b -> binary
+ -> read and write simultaneo
U -> Salto de linea
rb -> read binary
wb -> write binary
r+b -> read and write binary
'''

print('')
print('**********************************************************************')
print('LECTURA Y ESCRITURA DE ARCHIVOS 1')

# Abrir un archivo para lectura.

archivo = open('escrito.txt', 'r')
cadena1 = archivo.read(16) # Lee los primeros 16 caracteres.
print(cadena1)
print('---------------------------')
cadena2 = archivo.read() # Lee lo que queda de archivo.
print(cadena2)
archivo.close()

print('')
print('**********************************************************************')
print('LECTURA Y ESCRITURA DE ARCHIVOS 2')

# Vamos a leer linea a linea.

archivo = open('escrito.txt', 'r')

while True:
    linea = archivo.readline()
    if not linea: # Si no hay más lineas hace un break.
        break
    print(linea)
    print('---------------------------')

archivo.close() # Hay que hacer close para cerrar (como en java).

print('')
print('**********************************************************************')
print('LECTURA Y ESCRITURA DE ARCHIVOS 3')

# Vamos a leer linea a linea con un bucle for.

archivo = open('escrito.txt', 'r')

lista = archivo.readlines() # Lee todas las líneas y las guarda en una lista.
numlin = 0
for linea in lista:
    numlin += 1
    print('Linea', numlin, ':', linea)
print('')
print('Número de lineas del archivo:', numlin)
archivo.close()

print('')
print('**********************************************************************')
print('LECTURA Y ESCRITURA DE ARCHIVOS 4')

# Vamos a usar el with open para abrir el archivo.
# No hace falta cerrar.

with open('escrito.txt') as archivo:
    for linea in archivo:
        print(linea)

print('')
print('**********************************************************************')
print('LECTURA Y ESCRITURA DE ARCHIVOS 5')

# Vamos a leer y escribir.

cadena1 = 'Datos'
cadena2 = 'Secretos'

archivo = open('datos1.txt', 'w') # Si no existe el archivo lo crea y si existe lo sobreescribe.

archivo.write(cadena1 + '\n')
archivo.write(cadena2)

with open('datos1.txt') as archivo:
    for linea in archivo:
        print(linea)

print('')
print('**********************************************************************')
print('LECTURA Y ESCRITURA DE ARCHIVOS 6')

# Vamos a leer y escribir a partir de una lista.

lista = ['lunes ', 'martes ', 'miercoles ', 'jueves ', 'viernes ', 'sabado ', 'domingo ']
archivo = open('datos2.txt', 'w')
archivo.writelines(lista)

with open('datos2.txt') as archivo:
    for linea in archivo:
        print(linea)

# TODO: Hacemos un programa que pueda separar los elementos de la lista.

print('')
print('**********************************************************************')
print('LECTURA Y ESCRITURA DE ARCHIVOS 7')

# Vamos a leer a partir de la posición del puntero.

archivo = open('datos2.txt', 'r')
archivo.seek(5) # Puntero en la posición 5.
print('El puntero ha saltado a la posición:', archivo.seek(5))
cadena1 = archivo.read(5) # Lee los siguientes 5 caracteres.
print('Se leen los siguientes 5 caracteres:', cadena1)
print('El puntero está en la posición:', archivo.tell()) # Posición del puntero.
archivo.close()


