# -*- coding: utf-8 -*-

'''
Created on 8 nov 2022

@author: diego
'''

'''
VARIABLES
'''
print("PRUEBAS DE USO DE LAS VARIABLES")
#Las variables deben estar declaradas en el punto que le toca, porque si no puede
#interpretar que está dentro de un
#if o un for o un while.
num1 = 5
num2 = 7
print('La suma de', num1, 'y', num2, 'es:', num1 + num2)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE LAS VARIABLES 2")
#No hay problema que sean de tipo distinto siempre
#que sean valores claros y de tipo numerico.
num3 = 12.55
num4 = 5
print(num3 + num4)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE LAS VARIABLES 3")
var1 = "HOLA"
var2 = 'DAM'
print(var1 + var2)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE LAS VARIABLES 4")
print(5 == 8) #El resultado es false, ya que funciona como un booleano.
print("")
print(8 == 8) #El resultado es true.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE LAS VARIABLES 5")
print(3, 8 == 8 and 4 == 2) #Con que una sea falsa dará false.
print("")
print(3, 8 == 8 or 4 == 2) #Con que la primera sea True saldrá true.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE LAS VARIABLES 6")
print(7, 'a' == ('a' or 'b'))

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 1")
from datetime import date

fecha = date(2022, 11, 8)
print(fecha)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 2")
hoy = date.today()
print(hoy)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CONVERSION DE DATOS 1")
num1 = 5
num2 = 4.3
num3 = 20.8
num4 = "HOLA"
num5 = '2ºDAM'
num6 = "ALcobendas"

print('El tipo de dato de num1 es:', type(num1)) #Así vemos que tipo de variable es.
print('El tipo de dato de num2 es:', type(num2)) #Así vemos que tipo de variable es.
print('El tipo de dato de num3 es:', type(num3)) #Así vemos que tipo de variable es.
print('El tipo de dato de num4 es:', type(num4)) #Así vemos que tipo de variable es.
print('El tipo de dato de num5 es:', type(num5)) #Así vemos que tipo de variable es.
print('El tipo de dato de num6 es:', type(num6)) #Así vemos que tipo de variable es.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 2")
print(repr(num1)) #extrae el dato o caracter sin comillas
print('El tipo de dato de num1 es:', type(num1)) #Así vemos que tipo de variable es.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 3")
print(repr(num2)) #extrae el dato o caracter sin comillas
print('El tipo de dato de num2 es:', type(num2)) #Así vemos que tipo de variable es.

print("")
print("**********************************************************************")
print("*******************")
print("PRUEBAS DE USO DE CLASES/MODULOS 4")
print(repr(num4)) #extrae el dato o caracter sin comillas
print('El tipo de dato de num2 es:', type(num4)) #Así vemos que tipo de variable es.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 5")
var10 = '12'
print('El tipo de dato de var10 es:', type(var10))

var11=int(var10)
print('El tipo de dato de va11 es:', type(var11)) #Así casteamos.


print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 6")
print(repr(num4)) #Este lo que hace es convertir el valor de num4 en String.
print('El tipo de dato de num4 es: ', type(num4))

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 7")
var1 = '15' #Esto lo que hace es crear un String de valor 15
print(var1)
print(type(var1))
var2 = int(var1) #Esta es la manera de cambiar un String NUMERICO en un int.
print(var2)
print(type(var2))

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 8")
var3 = "25.76"
print(var3)
print(type(var3))
var4 = float(var3)
print(var4)
print(type(var3))

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 9")
var1 = 5
var2 = str(var1)
print(type(var1))
print(type(var2))

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 10")
var5 = 34.96
print("El tipo de var5 es: ", type(var5))
var6 = int(var5)
print(var6)
print("El tipo de var6 es: ", type(var6))
#Lo que hace al convertirlo en int quita los decimales SIN redondear.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE CLASES/MODULOS 11")
var6 = 33.67
print("El tipo de var6 es: ", type(var6))
var7 = str(var6)
print(var7)
print("El tipo de var6 es: ", type(var7))


print("")
print("**********************************************************************")
print("PRUEBAS FUNCION EVAL 1")
#Evalua el contenido de un string siempre que sea un valor numerico.
#Si metemos caracteres alfabeticos da ERROR!!!
v = eval("123")
print(v, 'es de tipo', type(v))

print("")
print("**********************************************************************")
print("PRUEBAS FUNCION EVAL 2")
v1 = eval("84.72")
print(v1, 'es de tipo', type(v1))

print("")
print("**********************************************************************")
print("PRUEBAS FUNCION EVAL 3 Listas")
v3 = eval("[2, 7, 5, 8]")
#Esta lista con corchetes puedes cambiarle el valor a su contenido, si fuera parentesis NO
print(v3, 'es de tipo', type(v3))

print("")
print("**********************************************************************")
print("PRUEBAS FUNCION EVAL 4 Listas")
v4 = eval("(2, 7, 5, 8)")
#Esta lista con corchetes puedes cambiarle el valor a su contenido, si fuera parentesis NO
print(v4, 'es de tipo', type(v4))

