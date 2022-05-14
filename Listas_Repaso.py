#Programa que registre los grados del clima
#Que saque el promedop
#Que muestre el primer dato ingresado
#Que muestreel ultimo dato ingresado
#Promedio de grados ingresados
#todo automatico
#Ingreso manual

import os

en_funcionamiento = True


while en_funcionamiento:
    grados = []
    promedio = 0.0
    primer_grado = 0.0
    ultimo_grado = 0.0
    variable_sumara = 0.0
    opciones = 0

    print("""
    1: Ingresar Programa
    2: Salir programa
    3: Mostrar Respuestas
    """)
    opciones = int(input("Ingrese el digito del menu: "))

    if opciones == 1:
        while True:
            grado = float(input("Indicame un Grado: "))
            grados.append(grado)
            variable_sumara += grado
            pregunta = input("Desea agregar un dato mas? S/N")

            if "s" in pregunta.lower():
                pass
            elif "n" in pregunta.lower():
                opciones = 3
                break

    elif opciones == 2:
        en_funcionamiento = False

    else:
        os.system("cls")
        input("Indique bien el digito por favor... ")

    if opciones == 3:
        try:
            primer_grado = grados[0]
            ultimo_grado = grados[len(grados)-1]
            promedio = variable_sumara / len(grados)
            print("""
            grados = {}
            promedio = {}
            primer_grado = {}
            ultimo_grado = {}
            """.format(grados,promedio,primer_grado,ultimo_grado))
        except IndexError as error:
            print("No Ha ingresado ningun dato")



        input("Precione para volver al menu ...")
        os.system("cls")
        




