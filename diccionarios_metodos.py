print("")
print("**********************************************************************")
print("PRUEBAS DE DICCIONARIOS CON MÉTODOS 1")


# Hay que crear las funciones que se van a llamar en el diccionario.
def uno():
    return 'Enero'


def dos():
    return 'Febrero'


def tres():
    return 'Marzo'


def cuatro():
    return 'Abril'


def cinco():
    return 'Mayo'


def seis():
    return 'Junio'


def siete():
    return 'Julio'


def ocho():
    return 'Agosto'


def nueve():
    return 'Septiembre'


def diez():
    return 'Octubre'


def once():
    return 'Noviembre'


def doce():
    return 'Diciembre'


def numeros_a_meses(argumentos):
    dicc = {
        1: uno(),
        2: dos(),
        3: tres(),
        4: cuatro(),
        5: cinco(),
        6: seis(),
        7: siete(),
        8: ocho(),
        9: nueve(),
        10: diez(),
        11: once(),
        12: doce()
    }
    func = dicc.get(argumentos,
                    'Mes invalido.')  # Si el argumento no está en el diccionario, nos devuelve 'mes invalido.'.
    print(func)


numeros_a_meses(2)
