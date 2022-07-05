import numpy as np
import sys


#programa que puedas iniciar session OK
#puedas registrar clientes
#puedes ver que usuario lo registro
#mostrar todos los usuarios

#nombre usuario y una contraseña
# rut nombre y edad
# buscar los rut

lista_usuario = ["mau"]
lista_contraseñas = ["12345"]
cuenta = False

cl_rut = []
cl_nombes = []
cl_edades = []

def buscar_contraseñas(lista_usuario, lista_contraseñas, usuario, contraseña):
    indice = 0
    for user in lista_usuario:
        if user == usuario:
            if lista_contraseñas[indice] == contraseña:
                return True
        indice += 1
    return False



while True:

    print("""
 [1] Iniciar Seccion
 [2] Crear un Clientes
 [3] Datos del Usuario
 [4] Salir   
    """)

    opciones = input("Dame la Opcion: ")

    if opciones == "1":
        for intentos in range(0, 3):
            usuario = input("dame el usuario: ")
            contraseña = input("dame la contraseña: ")
            cuenta = buscar_contraseñas(lista_usuario, lista_contraseñas, usuario, contraseña)
            if cuenta:
                break
        if cuenta == False :
            print("Se ha bloqueado el programa por demaciados intentos")
            input("Precione para continuar...")
            break

    elif opciones == "2":
        while True:
            if cuenta == False:
                print("No has iniciado seccion... ")
                input("Precione para continuar...")
                break

            try: 
                rut = input("Dame el rut del cliente: ")
                nombre = input( "Dame el nombre del cliente: ")
                edad = int(input("Edad del cliente: "))

                cl_rut.append(rut)
                cl_nombes.append(nombre)
                cl_edades.append(edad)
                pregunta = input("Quiere agregar otro? s/n")
                if not "s" in pregunta.lower():
                    break

            except ValueError as error:
                print("Error de valores intentalo nuevamente")

    elif opciones == "3":
        while True:
            if not cuenta:
                print("No has iniciado seccion... ")
                input("Precione para continuar...")
                break
            
            if not len(cl_rut) >= 1:
                print("No hay datos ingresados!... ")
                input("Precione para continuar...")
                break
                
            for indices in range(0, len(cl_rut)):
                print("""
                Rut: {}
                Nombre: {}
                Edad: {}
                """.format(cl_rut[indices], cl_nombes[indices], cl_edades[indices]))

            input("Precione para continuar... ")
            break





