#Generar una funcion dentro de un modulo que genere numeros aleatorios en una matriz retorne la matriz
#generar un motodo que imprima los datos
#importar el modulo desde una funcion main
#ejecutar el programa desde la raiz


def main():
    
    while True:
            
        try:
            a = int(input("Dame rango a: "))
            b = int(input("Dame rango b: "))

            nueva_lista = num.numeros_aleatorios(a,b)
            num.imprimir_arrays(nueva_lista)
            print(len(nueva_lista))
            break
        except ValueError as error:
            print(error)





main()
import Modulos.numeros as num