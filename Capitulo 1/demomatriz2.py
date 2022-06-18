import os
import numpy as np

edades = np.array([

                    [22, 5, 15],
                    [30, 7, 25],
                    [40, 35, 10]


                    
                    ])

for f in range(len(edades)):
    for c in range(len(edades[0])):
        print(edades[f][c], end = " ")
    print("")

    #imprimir todos los elementos menores e iguales a 20

print("Fin del Programa...")

cc = 0
espacio = " "
for f in range(len(edades)):
    for c in range(len(edades[0])):
        if edades [f] [c] <= 20:
            print(edades[f][c], end = " ")
    print("")


a = np.array([

                    [22, 12, 23],
                    [34, 25, 19],
                    [22, 21, 18]


                    
                    ])

b = np.array([
                    [2, 5, 2],
                    [3, 2, 9],
                    [4, 3, 8]
                    ])

suma = np.array([

                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]


                    
                    ])
for f in range(len(a)):
    for c in range(len(a[0])):
        print(edades[f][c], end = " ")
    print("")
for f in range(len(b)):
    for c in range(len(b[0])):
        print(edades[f][c], end = " ")
    print("")
print("/////////////////////// Suma de la libreria /////////////////////////////////////////")
for f in range(len(a)):
    for c in range(len(a[0])):
        suma[f][c] = a[f][c] + b[f][c]
