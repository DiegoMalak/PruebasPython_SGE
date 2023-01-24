# La primera vez que ejecuto una clase python, debo ejecutarla desde boton derecho sobre la clase
# y seleccionar la opcion "Run 'nombre de la clase'". Si la clase ya ha sido ejecutada, puedo ejecutarla.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES")

# BUCLE WHILE
# El bucle while se ejecuta mientras la condicion sea verdadera.
# Si la condicion es falsa, el bucle no se ejecuta.

a = 0
while a < 10:
    a += 1
    # Para que no haga salto de linea al poner el print, se pone end=""
    # y se pone un espacio en blanco al final del print.
    # Si en el espacio en blanco se pone un caracter, se pone ese caracter
    # al final de cada print, como si fuera un separador.
    print(a, end=" ")
    # print(a)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 2")

anio = 2010
while anio <= 2022:
    print("Informes del año", str(anio))
    anio += 1
    # Bucle que va incrementando el año hasta que llega a 2022.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 3")
# BUCLE INFINITO CON WHILE

while True:
    nombre = input("Introduce tu nombre: ")
    print("Hola", nombre)
    # En caso de que no se introduzca un nombre, el bucle se ejecuta infinitamente.
    # Si se introduce el nombre, entra en el if y por lo tanto hace el break.
    # Aunque el break hay que tratar de evitar su uso.
    if nombre:
        break
print()

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 4")
# BUCLE WHILE

# Inicializamos la variable vacia para que tenga un valor.
# y de esta forma interpreta de que tipo es su valor.
fin_prog = ""
while fin_prog != "s" and fin_prog != "S":
    print("Hola, ¿cómo estás?. Estas dentro del bucle while")
    # Si se introduce s o S, se sale del bucle, en caso de que introduzca otra letra,
    # se vuelve a ejecutar el bucle.
    fin_prog = input("¿Quieres salir del programa? (s/n): ")

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 5")
# BUCLE WHILE

fin_prog = ""
while fin_prog != ("s" or "S"):
    print("Hola, ¿cómo estás?. Estas dentro del bucle while")
    fin_prog = input("¿Quieres salir del programa? (s/n): ")

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 6")
print("BUCLE FOR")

lista = ['geranio', 'rosa', 'margarita', 'clavel', 'violeta']
for e in lista:
    print(e)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 7")
print("BUCLE FOR")

# Creamos una lista con flores.
lista = ['geranio', 'rosa', 'margarita', 'clavel', 'violeta']
# Hacemos un bucle for para recorrer la lista.
# La variable k es la que coge la posicion de cada elemento de la lista. (Número de la posición)
# la variable x es la que coge el valor de cada elemento de la lista. (Flor que hay en cada posición)
for k, x in enumerate(lista):
    print("Lista[", k, "] = ", x)


print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 8")
print("BUCLE FOR")

# Hacemos el bucle for con un rango de 1 a 3.
# El rango es de 1 a 3, porque el 3 no se incluye.
for e in range(1, 3):
    print(e)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 9")
print("BUCLE FOR")

# Creamos una lista con flores.
lista = ['geranio', 'rosa', 'margarita', 'clavel', 'violeta']
# Hacemos un bucle for para recorrer la lista, para que nos saque el rango del 1 al 3.
# Y nos mostrará las flores que hay en esas posiciones.
for e in range(1, 3):
    print(lista[e])

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 10")
print("BUCLE FOR")

# Creamos una lista con flores.
lista = ['geranio', 'rosa', 'margarita', 'clavel', 'violeta']

for e in range(len(lista)):
    print(lista[e])

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 11")
print("BUCLE FOR")

# Creamos una lista con flores.
lista = ['geranio', 'rosa', 'margarita', 'clavel', 'violeta']

# Con este bucle for, nos muestra desde la posicion 2 hasta el final de la lista
for e in range(2, len(lista)):
    print(lista[e])

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 12")
print("BUCLE FOR")

# Creamos una lista con flores.
lista = ['geranio', 'rosa', 'margarita', 'clavel', 'violeta']

# Con este bucle for, nos muestra todos los elementos de la lista, excepto los dos ultimos.
for e in range(len(lista) -2):
    print(lista[e])

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE BUCLES 13")
print("BUCLE FOR")

# Creamos una lista con numeros.
listanum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma = 0
for num in listanum:
    suma = suma + num
print("La suma de los numeros de la lista es: ", suma)



