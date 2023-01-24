print('Paquete cadenas.py para aprender los modulos de Python')
print('----------------------------------------------------')
print('')

# Vamos a hacer una funcion que nos devuelva una palabra y que
# nos dé una letra de esa palabra.
def dame(texto):
    print('La palabra es:', texto)
    for caracter in texto:
        print('Dame una letra:', caracter)
        print("'" + caracter + "'")

# Vamos a hacer una funcion que nos devuelva una palabra y que
# nos dé una letra del medio de esa palabra.
def medio(texto):
    print('El caracter que está en medio de', texto, 'es:', texto[len(texto)//2])

# Vamos a hcer que el texto que nos pasen lo pase a mayusculas sin usar la funcion upper().
# Se puede hacer en ASCII, con ayuda de ord() y chr().
def a_mayusc(texto):
    print('La palabra', texto, 'en mayusculas es:', end=' ')
    for caracter in texto:
        # if ord(caracter) >= 97 and ord(caracter) <= 122:
        if 97 <= ord(caracter) <= 122:
            print(chr(ord(caracter) - 32), end='')
        else:
            print(caracter, end='')

def a_mayusc2(texto):
    print('La palabra es:', texto)
    mayusc = ''
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            posicion = ord(caracter) - ord('a')
            nuevo_ascii = posicion + ord('A')
            caracter = chr(nuevo_ascii)
        mayusc = mayusc + caracter
    return mayusc

__version__ = '1.0'

'''
print('En mayúsculas:', a_mayusc2('Avatar: el sentido del agua.'))
print('----------------------------------------------------')
dame('Hola a todos')
print('----------------------------------------------------')
medio('AULAS')
'''
