print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 1")

# Creamos un diccionario de contactos.
contactos = {}
nombre = 'Isaac Newton'
numero = '123456789'
contactos[nombre] = numero

nombre = 'Albert Einstein'
numero = '987654321'
contactos[nombre] = numero

nombre = 'Marie Curie'
numero = '111111111'
contactos[nombre] = numero

print('********IMPRIMIMOS EL DICCIONARIO DE CONTACTOS********')
print(contactos)
print('******************************************************')
print('')

print('El telefono de Isaac Newton es:', contactos['Isaac Newton'])
print('El telefono de Albert Einstein es:', contactos['Albert Einstein'])
print('El telefono de Marie Curie es:', contactos['Marie Curie'])
print("")
print(contactos.keys()) # Nos muestra las claves (nombres) del diccionario.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 2")

# Recorrer un diccionario con un bucle for y mostrar los valores.
for nombre in contactos:
    print('Nombre:', nombre, 'Telefono:', contactos[nombre])

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 3")

# Recorrer un diccionario con un bucle for para borrar los valores.
#for nombre in contactos:
    #del contactos[nombre]

    #LO COMENTO PARA QUE NO SE BORREN LOS DATOS.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 4")

diccionario = {'nombre': 'Carlos' , 'edad': 25,
               'cursos': ['Python', 'Django', 'Flask']}

print('')
print(diccionario)

print('')
print('El nombre es:', diccionario['nombre'])
print('La edad es:', diccionario['edad'])
print('Los cursos son:', diccionario['cursos'])
print('')
print('El primer curso es:', diccionario['cursos'][0])
print('El segundo curso es:', diccionario['cursos'][1])
print('El tercer curso es:', diccionario['cursos'][2])

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 5")

for key in diccionario:
    print(key, ':', diccionario[key]) # Nos muestra las claves y los valores del diccionario separados por dos puntos.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 6")
print("CREAR DICCIONARIOS DE MANERA COMPLEJA")

dic = dict(zip('abc', [1, 2, 3, 4]))
print(dict) # Nos muestra de que tipo es dict.
print(dic) # Nos muestra el diccionario.
print(dic.keys()) # Nos muestra las claves del diccionario.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 7")
print("CREAR DICCIONARIOS DE MANERA COMPLEJA")

items = dic.items()
print(items) # Nos muestra los items del diccionario.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 8")
print("CREAR DICCIONARIOS DE MANERA COMPLEJA")

keys = dic.keys()
print(keys) # Nos muestra las claves del diccionario.
print('')
val = dic.values()
print(val) # Nos muestra los valores del diccionario.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 9")
print("CREAR DICCIONARIOS DE MANERA COMPLEJA")

valor = dic.get('b')
print("El valor de 'b' es", valor) # Nos muestra el valor de la clave 'b'.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 10")

dic1 = dic.copy() # Copiamos en dic1 el diccionario dic.
print(dic1) # Nos muestra el diccionario copiado.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 11")

valor = dic.pop('b') # Eliminamos el valor de la clave 'b'.
print(dic) # Nos muestra el diccionario sin el valor de la clave 'b'.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 12")

valor = dic.setdefault('a') # Nos muestra el valor de la clave 'a'.
print(valor) # Nos muestra el valor de la clave 'a'.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 13")

valor = dic.setdefault('d', 4) # Nos muestra el valor de la clave 'd'.
print(valor) # Nos muestra el valor de la clave 'd'.
print(dic) # Nos muestra el diccionario con el valor de la clave 'd'.

'''
valor = dic.setdefault('c', 60)
print(valor)
print(dic)
ESTO NO VA A FUNCIONAR POR LA KEY NO PUEDE ESTAR REPETIDA.
'''

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 14")

dic = dict.fromkeys(['a', 'b', 'c'], 1) # Nos crea un diccionario con las claves 'a', 'b' y 'c' y los valores 0.
print(dic) # Nos muestra el diccionario con sus nuevos valores.

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 15")

# Vamos a ver que teniendo dos diccionarios creados, mediante un update podemos unirlos.

dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic2 = {'b' : 9, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

dic1.update(dic2) # Unimos los dos diccionarios.
print(dic1) # Nos muestra el diccionario con los valores de los dos diccionarios.
# Vemos que si hay claves repetidas, se quedan con el valor del diccionario 2 ya que se actualiza
# con el valor indicado en el .update(dic2).

print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS 16")

# Vamos a limpiar el diccionario.
'''
dic1.clear() # Limpiamos el diccionario.
print(dic1) # Nos muestra el diccionario vacío.
'''







