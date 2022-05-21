import os

def imprimir(x):
    print(x)
    input("Precione para continuar")

def calculos(condicion,a,b):
    if condicion == "*":
        return a * b
    elif condicion == "+":
        return a + b
    elif condicion == "-":
        return a - b
    elif condicion == "/":
        try:
            return a / b
        except ZeroDivisionError as error:
            print("Hubo un error por que no se pudo dividir en 0")
            return 0
    elif condicion == "**":
        return a ** b

def solicitar_datos():
    try:
        a = int(input("Dame A: "))
        b = int(input("Dame B: "))
        return a, b
    except ValueError as error:
        print("Error de valor: ")
        return 0, 0

while False:
    opcion = input("""
BIENVENIDOS A MI CALCULADORA
[1] Multiplicar
[2] Sumar
[3] Restar
[4] Dividir
[5] Potencia
[0] Salir

Indique una Opcion: """)
    if opcion == "1":
        #resultado = solicitar_datos()
        #a = resultado[0]
        #b = resultado[1]
        a, b = solicitar_datos()
        resultado = calculos("*", a, b)
        imprimir(resultado)
    elif opcion == "2":
        a, b = solicitar_datos()
        resultado = calculos("+", a, b)
        imprimir(resultado)
    elif opcion == "3":
        a, b = solicitar_datos()
        resultado = calculos("-", a, b)
        imprimir(resultado)
    elif opcion == "4":
        a, b = solicitar_datos()
        resultado = calculos("/", a, b)
        imprimir(resultado)
    elif opcion == "5":
        a, b = solicitar_datos()
        resultado = calculos("**", a, b)
        imprimir(resultado)
    elif opcion == "0":
        break
    else:
        print("****Digito mal ****")
    os.system("cls")






#void 
def imprimir(x):
    resultado = 3424234234 * 2134123123
    tipado = [21312312,312312312,312,3,123,12,312,3,12,312,31,23]
    nombres= [",123123123123", "123123123123"]
    print(x)

def imprimir2(x):
    if x == 1:
        return "Si es 1"
    else:
        return "No es 1"

def imprimir2(x,b,c):
    return x+b+c

variable = imprimir2(2)
print(variable)



def methodo_uno(*args): #el uso de este es para asignar varias variables mas
    print(args) #Retorna lista

def methodo_dos(**kargs):# el uso de este es para enviar diccionarios o variable = valor
    print(kargs) #retorna diccionarios

methodo_uno(45,40,55,60,51) # asignacionaciones de multiples datos
methodo_uno(hola = 5, pepito=30) # asgnacion de un dict
