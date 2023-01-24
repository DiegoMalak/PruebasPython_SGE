'''
print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 1')
print('--> Función PASS')

# Función pass: No hace nada, es como un placeholder.

print('Aquí hay codigo comentado para que no se quede parado con el pass')
# while True:
# pass  --> Espera una interrupción de teclado (Ctrl+C)

# print('Esperando a que salga del while') # No se ejecuta.

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 2')
print('--> Función PASS')

for letra in 'Python':
    if letra == 'h':
        pass  # No hace nada, es para no dejar el código vacío y que pueda seguir corriendo.
        print('Esta es la letra', letra)
    print('La letra actual es', letra)

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 3')
print('--> Función DEF')

# Función def: Define una función.
def prueba():
    pass
    print('Esto es una prueba')

prueba()

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 4')
print('--> Función DEF')

def obtener_info(*args):
    pass  # No hace nada, podemos dejarlo o comentarlo.
    print('Este es el bloque pass')
    if args == ():
        print('No se ha pasado ningún argumento')
    else:
        print('Se ha pasado el argumento', args)

obtener_info()
obtener_info(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 5')
print('--> Función DEF')

def obtener_info(*args):
    print('Este es el bloque pass')
    if args == ():
        print('No se ha pasado ningún argumento')
    else:
        print('Se ha pasado el argumento', args)

obtener_info()
obtener_info(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
obtener_info('Hola', 'Mundo', 'Python', 3, 4, 5)

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 6')
print('--> Función DEF')

# Función def: Define una función.
# Esta función devuelve el valor de la suma de los dos argumentos.
def imprime(cadena):
    # Lo que hace la funcion es imprimir la cadena que le pasamos.
    print(cadena)
    # Devolvemos el valor de la cadena.
    cadena = cadena + 'FIN CADENA'
    # Devolvemos el valor de la cadena.
    return cadena

# Llamamos a la función imprime y le pasamos la cadena 'Primera cadena'.
imprime('Primera cadena')

# Llamamos a la función imprime y le pasamos la cadena 'Segunda cadena'.
var = imprime('Segunda cadena')
var2 = imprime(cadena = 'Tercera cadena')

print(var)
print(var2)

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 7')
print('--> Función DEF')

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

suma1 = suma(5, 7) # Hace la suma de 5 + 7.
print(suma1) # Imprime el resultado de la suma.

print(suma(15, 8)) # Llamamos a la función suma y le pasamos los argumentos 15 y 8.

suma2 = suma("6", "9") # Concatenamos los dos argumentos.
print(suma2) # Imprime el resultado de la suma.

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 8')
print('--> Función DEF')

def muestra_info(arg1, *valores):
    print('La salida de la función es:')
    print(arg1)
    for val in valores:
        print(val)

muestra_info(100)
muestra_info(90, 48, 36, 78)
muestra_info()

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 9')
print('--> Función DEF')

def actualizame(milista):
    milista.append([1, 2, 3, 4])
    print('La lista interna es:', milista)

milista = [10, 20, 30, 40]
actualizame(milista)
print('La lista externa es:', milista)

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 10')
print('--> Función DEF')

def actualizame(milista):
    milista = [1, 2, 3, 4]
    print('La lista interna es:', milista)

milista = [10, 20, 30, 40]
actualizame(milista)
print('La lista externa es:', milista)

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 11')
print('--> Función DEF')

def f(n, L = []): # L es una lista vacía.
    L.append(n) # Añadimos el valor de n a la lista.
    return L # Devolvemos la lista.

print(f(1)) # L = [1]
print(f(2)) # L = [1, 2]
print(f(3)) # L = [1, 2, 3]

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 12')
print('--> Función DEF')

def f(n, L = None): # L es una lista está en None y cuando vuelve la lista se deshace.
    if L is None: # Si L es None.
        L = [] # L es una lista vacía.
    L.append(n) # Añadimos el valor de n a la lista.
    return L # Devolvemos la lista.

print(f(1)) # L = [1]
print(f(2)) # L = [2]
print(f(3)) # L = [3]

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 13')
print('--> Función DEF')

def preguntar(mensaje, intentos = 4, aviso = 'Opción no válida. Prueba de nuevo!'):
    while True:
        opcion = input(mensaje)
        if opcion in ('s', 'S', 'si', 'SI', 'Si'):
            print('Has dicho que si.')
            return True
        if opcion in ('n', 'N', 'no', 'NO', 'No'):
            print('Has dicho que no.')
            return False
        intentos -= 1
        print('Te quedan', intentos, 'intentos.')
        if intentos == 0:
            raise ValueError('Opción no válida.')
        print(aviso)

# Una opción de hacer de otra manera la función preguntar.
# preguntar('¿Quieres sobreescribir?', 2, 'Solo debes decir si o no.')
#preguntar('¿Quieres sobreescribir el archivo?')
preguntar('¿Quieres sobreescribir el archivo papi?', aviso = 'Solo debes decir si o no.')

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 14')
print('--> Función DEF')

def loro(voltaje, estado = 'tieso', accion = 'explotar', tipo = 'Azul Nordico'):
    print('-- Este loro no va a', accion, end = ' ') # end = ' ' es para que no salte de línea.
    print('si haces pasar', voltaje, 'voltios a través de él') # 'voltaje' es una variable.
    print('-- Con un plumaje maravilloso y de tipo', tipo + ',') # 'tipo' es una variable.
    print('se quedaría', estado, '!') # 'estado' es una variable.

#loro(1000) # 1 argumento posicionado.
#loro(voltaje = 1000) # 1 argumento nombrado.
#loro(voltaje = 1000000, accion = 'BOOOOOM') # 2 argumentos nombrados.
#loro(accion = 'BOOOOOM', voltaje = 1000000) # 2 argumentos nombrados.
loro('un millón', 'despojado de vida', 'saltar') # 3 argumentos posicionados.
#loro('mil', estado = 'en un estado de coma') # 1 argumento posicionado, 1 argumento nombrado.

# SI NO NOMBRAMOS LA VARIABLE, SE TIENE QUE PONER EN EL ORDEN QUE SE DECLARAN EN LA FUNCIÓN.
# SI NOMBRAMOS LA VARIABLE, PODEMOS PONERLA EN CUALQUIER ORDEN.
'''

print('')
print('**********************************************************************')
print('FUNCIONES EN PYTHON 15')
print('--> Función EMBEBIDA')

def prueba_ambito(): # Función.
    def ambito_local(): # Función anidada.
        varprueba = 'local varprueba' # Variable local.

    def ambito_nonlocal(): # Función anidada.
        nonlocal varprueba # Variable no local.
        varprueba = 'nonlocal varprueba' # Variable no local.

    def ambito_global(): # Función anidada.
        global varprueba # Variable global.
        varprueba = 'global varprueba' # Variable global.

    varprueba = 'test varprueba' # Variable local. Sobreescribe a la variable local.
    ambito_local() # Llamamos a la función anidada.
    print('Puesta como local:', varprueba) # Imprimimos la variable local de dos líneas arriba.
    ambito_nonlocal() # Llamamos a la función anidada.
    print('Puesta como nonlocal:', varprueba) # Imprimimos la variable no local.
    ambito_global() # Llamamos a la función anidada.
    print('Puesta como global:', varprueba) # Imprimimos la variable global. Esta variable se
                                            # leería de manera global si estuviera fuera de la
                                            # función principal.

prueba_ambito() # Llamamos a la función.
print('En un ámbito global:', varprueba) # Imprimimos la variable global. Esta variable se lee
                                        # de manera global, ya que está fuera de la función principal.










