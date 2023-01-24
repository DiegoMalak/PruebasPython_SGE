'''
Created on 15 nov 2022

@author: diego
'''

print("")
print("**********************************************************************")
print("PRUEBAS FUNCION 1 Listas")
v3 = eval("[2, 7, 5, 8]")
#Esta lista con corchetes puedes cambiarle el valor a su contenido, si fuera parentesis NO
print(v3, 'es de tipo', type(v3))

print("")
print("**********************************************************************")
print("PRUEBAS FUNCION 2 Listas")
v4 = eval("(2, 7, 5, 8)")
#Esta lista con corchetes puedes cambiarle el valor a su contenido, si fuera parentesis NO
print(v4, 'es de tipo', type(v4))

print("")
print("**********************************************************************")
print("PRUEBAS LISTAS 1")
#ESTO SON LISTAS PROTEGIDAS O TUPLAS
mitupla = ("aa", 6, 'BB', 7.2, "aa", 3.98, 6, 'adios')
print(mitupla)
print(type(mitupla))

print("")
print("**********************************************************************")
print("PRUEBAS LISTAS 2")
#LISTA NO PROTEGIDA

milista = ["curso", 6, 'DAM', 'BB', 7.2, "BARCO", 3.89, 6, 'adios', 6]
print(milista)
print(type(milista))

print("")
print("**********************************************************************")
print("PRUEBAS LISTAS 3")
#ESTO ES PARA VER LA LONGITUD DE DICHA LISTA.
print(len(milista))
print(milista.__len__())

print(len(mitupla))
print(mitupla.__len__())

print("")
print("**********************************************************************")
print("PRUEBAS LISTAS 4")
print(milista[1:3]) #VEO LOS ELEMENTOS DESDE EL PRIMER NUMERO HASTA EL ANTERIO DE LA DERECHA EN ESTE CASO DEL 1 AL 2 (el 3 no)
print(milista[0:15]) #Mostraria de la 0 a la 14
print(milista[:]) #Lo muestra todo

print("")
print("**********************************************************************")
print("PRUEBAS LISTAS 5")

print(milista[2:]) #De la posicion 2 al final
print(milista[4:]) #De la posicion 4 al final
print(milista[:4]) #De la primera posicion hasta antes del 4.

print("")
print("**********************************************************************")
print("PRUEBAS LISTAS 6")

print(milista[1]) #ESTO ES COMO JAVA LA POSICION 1 ES LA SEGUNDA.

print("")
print("**********************************************************************")
print("PRUEBAS LISTAS 7")
#Vamos a ver en que posicion esta el valor que ponemos
print('Posicion', milista.index('BB'))
print('Posicion', milista.count(6))
