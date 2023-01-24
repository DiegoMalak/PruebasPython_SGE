print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES DE UNA DIMENSION 1")

matrizdim1 = []
for i in range(10):
    matrizdim1.append(1)
    # print(matrizdim1[i])
print(matrizdim1)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES DE UNA DIMENSION 2")

# Vamos a imprimir 12 elementos de valor 0
matrizdim1_2 = [0 for i in range(12)]
print("Imprimimos la lista con 12 ceros:\n", matrizdim1_2)

# Si quisieramos que una posicion de la matriz tuviera un valor distinto, lo haríamos de la siguiente manera:
matrizdim1_2[1] = 25
print("Imprimimos la lista con 12 ceros dandole a la posicion 1 el valor 25:\n", matrizdim1_2)

# Si quisieramos ver el valor de una posicion de la matriz, lo haríamos de la siguiente manera:
print("Vamos a ver el valor de la posicion 1:\n", matrizdim1_2[1])

print("Vamos a ver los valores 1 y 2 de la lusta:\n", matrizdim1_2[1:3])  # Nos muestra los valores de la posicion 1 y 2
print("Vamos a ver los valores 1, 2, 3 y 4:\n", matrizdim1_2[1:5])  # Nos muestra los valores de la posicion 1, 2, 3 y 4
print("Vamos a ver los valores hasta el 3 sin incluirlo:\n",
      matrizdim1_2[:3])  # Nos muestra los valores de la posicion 0, 1 y 2

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES DE UNA DIMENSION 3")

matrizdim1_3 = [i for i in range(12)]
print("Imprimimos la lista con 12 numeros del 0 al 11:\n", matrizdim1_3)

matrizdim1_4 = [i * i for i in range(12)]
print("Imprimimos la lista con 12 numeros del 0 al 11 elevados al cuadrado:\n", matrizdim1_4)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES BIDIMENSIONALES 1")

matrizdim2 = [[1, 3], [4, 6]]
print("Imprimimos la matriz bidimensional:\n", matrizdim2)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES BIDIMENSIONALES 2")

# Vamos a crear la matriz bidimensional y vamos a leer valor por valor
# segun su posicion en la matriz.

matrizdim2_2 = [[1, 3], [4, 6]]
print("Imprimimos la matriz bidimensional:\n", matrizdim2_2)

for i in range(len(matrizdim2_2)):
    for j in range(len(matrizdim2_2[i])):
        print("El valor de la posicion", i, ",", j, "es:", matrizdim2_2[i][j])

print("")
print("Otra forma de imprimirlo es:")
for row in range(len(matrizdim2_2)):
    for col in range(len(matrizdim2_2[row])):
        print("El valor de la posicion", matrizdim2_2[row][col], end=" ")
    print()

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES BIDIMENSIONALES 3")

matriz = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4]]
print("Imprimimos la matriz bidimensional:\n", matriz)  # Imprime la matriz bidimensional

matriz = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]  # el valor de x no puede ser igual al de y
print("Imprimimos la matriz bidimensional:\n", matriz)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES BIDIMENSIONALES 4")

matriz1 = [[0 for i in range(3)] for j in range(3)]
print("Imprimimos la matriz bidimensional:\n", matriz1)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES BIDIMENSIONALES 5")

matriz2 = [[i * j for j in range(3)] for i in range(3)]
print("Imprimimos la matriz bidimensional:\n", matriz2)
# En primer lugar, i coge el valor 0 y se multiplica por 0, 1 y 2 (que es el valor que va teniendo j)
# En segundo lugar, i coge el valor 1 y se multiplica por 0, 1 y 2 (que es el valor que va teniendo j)
# En tercer lugar, i coge el valor 2 y se multiplica por 0, 1 y 2 (que es el valor que va teniendo j)

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES BIDIMENSIONALES 6")

columna0 = [row[0] for row in matriz2]
print("Imprimimos la columna 0 de la matriz bidimensional:\n", columna0)
# En primer lugar, row[0] coge el valor 0 de la fila 0
# En segundo lugar, row[0] coge el valor 0 de la fila 1
# En tercer lugar, row[0] coge el valor 0 de la fila 2

print("")
print("SEGUNDA FORMA DE HACER LO ANTERIOR")
columna0 = [row[0] for row in matriz2]
print(columna0, end=" ")
print()
for e in matriz2:
    print(e, end=" ")
print()
# De esta manera se imprime la matriz bidimensional
# En primer lugar vamos a imprimir las columnas 0 de la matriz bidimensional
# En segundo lugar vamos a imprimir la matriz bidimensional completa con sus filas y columnas.

print("")
print("**********************************************************************")
print("PRUEBAS DE USO DE MATRICES BIDIMENSIONALES 7")

matriz = [[i + j for j in range(3)] for i in range(3)]

print("Imprimimos la matriz bidimensional:\n", matriz)
# En primer lugar, i coge el valor 0 y se suma 0, 1 y 2 (que es el valor que va teniendo j)
# En segundo lugar, i coge el valor 1 y se suma 0, 1 y 2 (que es el valor que va teniendo j)
# En tercer lugar i, coge el valor 2 y se suma 0, 1 y 2 (que es el valor que va teniendo j)

columna2 = [row[0] for row in matriz]
print("Imprimimos la columna 2 de la matriz bidimensional:\n", columna2)
