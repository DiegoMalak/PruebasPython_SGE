print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 1")

# Break

for letra in 'Python':
    if letra == 'o':
        break
    print('Letra obtenida en este paso: ', letra)

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 2")

# Continue

for letra in 'Python':
    if letra == 'h':
        continue
    print('Letra obtenida en este paso: ', letra)

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 3")

# Break: Va a hacer un bucle del 10 al 0, pero cuando llegue al 5, va a parar el bucle.
# Al tener el print antes del 'var -1', lo que va a hacer es mostrar el diez
# ya que se salta la condicion de var -1.
var = 10
while var > 0:
    print('Valor actual de la variable en este paso: ', var)
    var = var -1
    if var == 5:
        break

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 4")

# Continue: Va a hacer un bucle del 10 al 0, pero cuando llegue al 5, va a saltar el 5 y seguirá con el 4.
# Al tenner el print después del var -1, lo que va a hacer es cumplir la linea de 'var -1'.
var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('Valor actual de la variable en este paso: ', var)

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 5")

# Encontrar el número par.

print("Encontrar el número par")
for num in range(2, 25):
    if num % 2 == 0:
        print("El número par encontrado: ", num)
        continue # Continua con la siguiente iteracion.
    print('Número:', num)

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 6")

# Encontrar el número primo.

print("Encontrar el número primo")
for num in range(10, 20): # Para iterar entre 10 y 20.
    for i in range(2, num): # Para iterar entre 2 y num.
        if num % i == 0: # Determina el primer factor.
            j = num / i # Calcula el segundo factor.
            print('%d es igual a %d * %d' % (num, i, j)) # Imprime el resultado.
            break # Para ir al siguiente numero.
    else: # Si no se encuentra ningún factor.
        print(num, 'es un número primo') # Imprime el numero primo.

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 7")

# Saber que numero es par o impar.

print("Saber que numero es par o impar")
numero = 70 # Si ese valor es 50 se para y si es 100 se sale del bucle.
while numero < 100:
    if numero == 50:
        break
    if numero % 2 == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")
    numero = numero + 1
    continue
    print('Esto nunca se ejecuta...')
else:
    print('Se sale del bucle... cuando el valor de número sea 100...')

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 8")

# For y else con continue.

colores = ['negro', 'blanco', 'rojo', 'verde', 'azul', 'amarillo']
for color in colores:
    if color == 'verde':
        continue
    print('El ', color, ' es un color.')
else:
    print('No hay más colores.')

print("")
print("**********************************************************************")
print("PRUEBAS DE BUCLES BREAK-CONTINUE 9")

#for y else con break.

colores = ['negro', 'blanco', 'rojo', 'verde', 'azul', 'amarillo']
for color in colores:
    if color == 'verde':
        break
    print('El ', color, ' es un color.')
else:
    print('No hay más colores.')






