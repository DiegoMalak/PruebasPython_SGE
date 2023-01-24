# La primera vez que ejecuto una clase python, debo ejecutarla desde boton derecho sobre la clase
# y seleccionar la opcion "Run 'nombre de la clase'". Si la clase ya ha sido ejecutada, puedo ejecutarla.
# Clase para hacer el escanner.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE SCANNER")

# como solo ponemos un input, el scanner nos devuelve un string
# si queremos que nos devuelva un numero, debemos convertirlo
# con la funcion int() o float(). Si queremos que nos devuelva
# un booleano, debemos convertirlo con la funcion bool().

num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")
print('El tipo de dato de num1 es:', type(num1))
print('El tipo de dato de num2 es:', type(num2))
suma = num1 + num2
print("La suma de los dos números es: ", suma)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE SCANNER 2")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
print("La suma de los dos números redondeado es: ", round(suma, 2))
if suma < 10:
    print("La suma es MENOR que 10")
elif suma == 10:
    print("La suma es IGUAL a 10")
else:
    print("La suma es MAYOR que 10")








