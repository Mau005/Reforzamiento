#Crear una aplicación científica que agrege las temperaturas, el programa solicitará
#El nombre y apellido de quién guardara las temperaturas,
#Al terminar de agregar las temperaturas
#Debe mostrar la mínima registrada y la máxima registrada, 
#Debe tener el promedio aproximado de temperatura
#Debe mostrar todas las temperaturas de menor a mayor mostrar los datos del usuario
#Sacar promedio = sumar todas las variables y dividirlas por la 

#while True:
import os
os.system("cls")

while True: #Bucle principal
    
    nombre = ""
    apellido = ""
    temperaturas = []
    min_temperatura = 0.0
    max_temperatura = 0.0
    promedio = 0.0
    ordenamiento_temperaturas = []

    programa_funcionando = True
    condiciones_cumplidas = False
    print("""
    #Controles de Temperatura 100% Real No Feak HD 4k
    [1] Ingresar temperatura
    [2] salir del programa
    
    """)
    opciones = input("Indiqueme la Opcion: ")

    if opciones == "1":
        nombre = input("Dame tu nombre: ")
        apellido = input("Dame tu Apellido: ")
        programa_funcionando = True
        while programa_funcionando:
            try:
                aux = float(input("Dame la temperatura: "))
                temperaturas.append(aux)
                #if "s" in opcion_sub_menu.lower():
                condiciones_cumplidas = True
                while True:
                    opcion_sub_menu = input("Quieres agregar mas? S/N: ")
                    if opcion_sub_menu.lower() == "s" or opcion_sub_menu.lower() == "si":
                        break
                    elif opcion_sub_menu.lower() == "n":
                        programa_funcionando = False
                        break
                        
                    else:
                        print("Indique bien el caracter")
                condiciones_cumplidas = True

            except ValueError as error:
                print(f"Error de valores indique nuevamente {error}")
            
    elif opciones == "2":
        break
        
    if condiciones_cumplidas:
        min_temperatura = 0.0
        max_temperatura = 0.0

        for elemento in temperaturas:
            promedio += elemento
        promedio /= len(temperaturas)
        #promedio = promedio / len(temperaturas)
        ordenamiento_temperaturas = temperaturas.copy()
        ordenamiento_temperaturas.sort()
        
        min_temperatura = ordenamiento_temperaturas[0]
        max_temperatura = ordenamiento_temperaturas[len(ordenamiento_temperaturas) -1]
        os.system("cls")
        print("""
        Nombre: {}
        Apellido: {}
        Promedio: {}
        Minimo Temperatura: {}
        Maximo Temperatura: {}
        Temperaturas Ingresadas: {}
        Temperaturas Ordenadas: {}
        """.format(nombre, apellido, promedio, min_temperatura, max_temperatura,
        temperaturas, ordenamiento_temperaturas))

        input("Precione para continuar ...")
        os.system("cls")
        condiciones_cumplidas = False


print("Ha finalizado la aplicacion Se an guardado los datos")
