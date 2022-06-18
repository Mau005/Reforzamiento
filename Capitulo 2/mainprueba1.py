#Nuestro entorno de desarrollo
#import Modulos.Herramientas as mh
from Modulos.Herramientas import imprimir as imp, sumar as sum
from Modulos.Prueba2.generarNumeros import numeros_aleatorios as na


def main():
    while True: 
        print("Bienvenido a mi calculadora")

        try:
            a = int(input("Dame un numero para A"))
            b = int(input("Dame un numero para B"))

            imp("___________________________")
            imp("Los numeros son: " +  str(sum(a, b)))

        except ValueError as error:
            print(f"Escoje el numero correctamente {error}")



print(main)


print("test")


print("finaliza")