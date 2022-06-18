#Un Menu que registre 5 datos
# primer dato para asignar nombre
# segundo dato para asignar apellido
# tercer dato asginar un salario
# cuarto dato asignar su gasto hormiga
# preguntar si quiere salir
# al salir debe mostrar los datos ingresados

import os
os.system("cls")

en_funcionamiento = True #Indicamos mediante una variable si el programa funciona


while en_funcionamiento: #Esto es igual a en_funcionamiento == True
    #Asignamos las variables cada vez que inicia el bucle por personas
    nombre = ""
    apellido = ""
    salario = 0.0
    gasto_hormiga = 0.0
    opciones = ""
    calculo = 0.0

    print("""
1: Abrir Programa
0: SALIR
    """)#IMprimimos el Menu
    opciones = int(input("Dame una Opciones: ")) #Cargamos el menu

    if opciones != 0: #Si marca cualquier opcion que sea distinto a 0 inicia el programa
        nombre = input("Dame tu nombre: ")
        apellido = input("Dame tu apellido: ")
        salario = float(input("Dame tu salario"))
        gasto_hormiga = float(input("Dame tu gasto hormiga"))
        calculo = salario-gasto_hormiga #se calcula el gasto hormiga

        print("""
        Nombre: {}
        Apellido: {}
        Salario: {}
        Gasto Hormiga: {}
        Total del Sueldo: {}
        """.format(nombre,apellido,salario,gasto_hormiga,calculo)) #se imprime el gasto hormiga

        input("Precione para continuar...") #generamos un input solo para preguntar que precione algo no se asigna nada
        os.system("cls") # limpiamos pantalla y se vuelve a generar el bucle

    else:
        print("Rompemos el bucle") #Rompemos el bucle por su condicion y no rompiendo con un brak abruptamente
        en_funcionamiento = False
