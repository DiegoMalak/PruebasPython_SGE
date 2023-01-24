# La primera vez que ejecuto una clase python, debo ejecutarla desde boton derecho sobre la clase
# y seleccionar la opcion "Run 'nombre de la clase'". Si la clase ya ha sido ejecutada, puedo ejecutarla.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE IF")

semaforo = "verde"

if semaforo == "verde":
    print("Puedes pasar")
elif semaforo == "amarillo":
    print("Puedes pasar con precaución")
else:
    print("No puedes pasar")

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE IF 2")
# Valores absolutos

n = -8
if n < 0:
    print("El valor absoluto de", n, "es", -n)
else:
    print("El valor absoluto de", n, "es", n)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE IF 3")
# Mayor menor o igual

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 < num2:
    print(num1, "es menor que", num2)
elif num1 > num2:
    print(num1, "es mayor que", num2)
else:
    print(num1, "es igual que", num2)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE IF 4")
# Comprobacion de listas

lista = ['geranio', 'rosa', 'margarita', 'clavel', 'violeta']

if 'rosa' in lista:
    print("La rosa está en la lista")
else:
    print("La rosa no está en la lista")

if 'lirio' not in lista:
    print("El lirio no está en la lista")
    # añadimos el lirio a la lista en caso de que no esté.
    lista.append('lirio')
    print("Se ha añadido el lirio a la lista")
    print(lista)
else:
    print("El lirio está en la lista")

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE IF 5")










