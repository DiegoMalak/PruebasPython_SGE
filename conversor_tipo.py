# La primera vez que ejecuto una clase python, debo ejecutarla desde boton derecho sobre la clase
# y seleccionar la opcion "Run 'nombre de la clase'". Si la clase ya ha sido ejecutada, puedo ejecutarla.

print("")
print("**********************************************************************")
print('MANERA 1 DE CONVERTIR UN ENTERO A BINARIO')

# Le pido a un usuario que introduzca un numero entero
# y lo convierta en un numero binario, mediante divisiones sucesivas
# por 2. El resto de cada division se almacena en una lista.

# Pedimos al usuario que introduzca un numero entero.
num = int(input("Introduce un número entero: "))
# Hacemos un print para que el usuario vea el numero que ha introducido.
print('El número entero introducido es: ', num)

# Creamos una lista vacia para almacenar los restos de las divisiones.
binario = []

# Mientras el numero sea mayor que 0, se ejecuta el bucle.
while num > 0:
    # Calculamos el resto de la division por 2.
    binario.append(num % 2)
    # Calculamos el cociente de la division por 2.
    num = num // 2
# Imprimimos la lista binario, tenemos que darle la vuelta para que se vea bien,
# ya que la lista se va rellenando de derecha a izquierda de la division.
binario.reverse()

# Imprimimos la lista binario.
print("El número convertido a binario es: ", end="")

# Recorremos la lista binario e introducimos cada elemento en la variable i.
for i in binario:
    # Imprimimos cada elemento de la lista binario.
    print(i, end="")

'''
Otra manera de hacerlo mediante un casting a bin.
num = int(input("Introduce un numero entero: "))
print("El numero introducido es: ", num)
print("El numero introducido en binario es: ", bin(num))
'''

print("")
print("**********************************************************************")
print('MANERA 2 DE CONVERTIR UN ENTERO A BINARIO')

decimal = int(input("Introduce un número decimal, base 10, para convertir a binario: "))
binario = ''
while decimal // 2 != 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
print("El número decimal convertido a binario es: ", str(decimal) + binario)














