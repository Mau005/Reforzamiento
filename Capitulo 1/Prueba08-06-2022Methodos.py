import os
os.system("cls")
#	Patente ·string
#•	Marca · string
#•	Color · stirng
#•	Año Fabricación: (número entre 1900 y 2021) entero
#•	Tipo vehículo solo puede aceptar como caracteres las letras b, d, e, h (bencina, diesel, eléctrico, híbrido)

#El menú debe tener las siguientes opciones: 
#1.	Registrar automóvil. 
#2.	Registro Mantenimiento. 
#3.	Consultar Automóvil. 
#4.	Listado General de Autos atendidos (Mantenciones).
#5.	Listado de autos atendidos en una fecha específica.
#6.	Listado de autos atendidos por concepto de mantención.
#7.	Salir. 




def comprobacion_basio(argumento):
    return not argumento == "" # retorna true si tiene contenido

def comprobacion_caracteres(argumento, condicion):
    return argumento in condicion

def buscar_auto_existente(lista, dato_buscar):
    for elementos in lista:
        if dato_buscar == elementos:
            return True # retorna si encontro algo
    return False #retorna si no encontro nada

def buscar_automovil(lista,dato_buscar):
    contador = 0
    for elementos in lista:
        if dato_buscar == elementos:
            auto = """
                patente: {}
                Modelo: {}
                Color: {}
                Año: {}
                Combustible: {}
                """.format(lista[contador], lista[contador +1], lista[contador + 2], lista[contador + 3], lista[contador + 4])
            return auto
        contador +=1
    return "No se ha encontrado el vehiculo"

def buscar_por_indice(lista):
    cantidad_mantenimientos = int(len(lista) / 3)- 1 #Si cada 3 elementos en 1 lista corresponde a un vehiculo, lo devidido por la longitud de la lista para determinar cuantos vehiculos tengo, -1 por que buscaremos indices de una lista
            
    for vehiculo in range(0,cantidad_mantenimientos):
        posicion_actual = cantidad_mantenimientos* vehiculo
        mantemiento = """
        patente: {}
        Fecha Ingreso: {}
        Observaciones: {}
        """.format(lista[posicion_actual], lista[posicion_actual +1], lista[posicion_actual + 2])
        print(mantemiento)

def ingresar_fechas():
    while True:
        try:
            fecha_dia = int(input("Ingrese el dia: "))
            fecha_mes = int(input("indicame el numero de mes: "))
            fecha_año = int(input("Indiqueme el Año: "))

            if len(str(fecha_dia)) == 1:
                fecha_dia = f"0{fecha_dia}"
            if len(str(fecha_mes)) == 1:
                fecha_mes = f"0{fecha_mes}"

            formato_fecha = f"{fecha_dia}-{fecha_mes}-{fecha_año}"
            break
        except ValueError:
            print("Error al digitar las Fechas")
    return formato_fecha

def buscar_mantenimiento(lista,buscar):
    contador = 0
    for elementos in lista:
        if buscar in str(elementos):
            print("""
                    patente: {}
                    Fecha Ingreso: {}
                    Observaciones: {}
                    """.format(lista[contador - 2], lista[contador- 1], lista[contador]))
        
        contador += 1

def listados_general(lista, cantidad_argumentos):
    cantidad_elementos = int(len(lista) / cantidad_argumentos) #Si cada x elementos en 1 lista corresponde a un vehiculo, lo devidido por la longitud de la lista para determinar cuantos vehiculos tengo, -1 por que buscaremos indices de una lista
    contador = 0
    print(f"Cantidad de elementos {cantidad_elementos}")
    for elementos in range(0, cantidad_elementos):
        posicion_actual = elementos * cantidad_elementos

        for datos in range(posicion_actual, (posicion_actual+cantidad_argumentos) - 1):
            print(f"Mi Indice es: {datos}")
            print(lista[datos])
        print("_______________________")
        contador += 1

automoviles = ["abcd12","Kia", "azul francia", 2020,"b",
             "hjfd02","Chavrolet", "plateado",2018,"d",
             "dfgl03","MG","Rojo electrico",2019, "h"]

lista = ["abcd12", 2-5-2020, "cambio de aceite",
             "hjfd02",10-4-2019,"lavado de motor",
             "dfgl03",29-8-2020,"Manrencion general"]

while True:

    print("ServiExpress")
    print("""
    #1.	Registrar automóvil. 
    #2.	Registro Mantenimiento. 
    #3.	Consultar Automóvil. 
    #4.	Listado General de Autos atendidos (Mantenciones).
    #5.	Listado de autos atendidos en una fecha específica.
    #6.	Listado de autos atendidos por concepto de mantención.
    #7.	Salir. 
    """)
    opcion = input("Ingreseme donde quiere ingresar: ")
    if opcion == "1":
        while True:
            patente = input("Dame la patente: ")
            if len(patente) == 6:
                break
            else:
                os.system("cls")
                print("Ingrese la patente como corresponde: ")
        
        while True:
            marca = input( "Dame la marca: ")
            if comprobacion_basio(marca):
                break

        while True:
            color = input("Dame el Color: ")
            if comprobacion_basio(color):
                break
        
        while True:
            try:
                fabricacion = int(input("Dame el año del vehiculo: "))

                if fabricacion >= 1900 and fabricacion <= 2021:
                    break
                else:
                    os.system("cls")
                    print("Indique el Año correspondiente entre 1900 - 2021")
            except ValueError as error:
                print(f"Error {error} Indique nuevamente el problema")

        while True:
            bencina   = input("Indiqueme el tipo de combustible: ")
            if comprobacion_caracteres(bencina,"bdeh"):
                break
        print(f"Se ha registrado el vehiculo: Patente: {patente}, marca: {marca}, color: {color}, Año Fabricacion: {fabricacion}, Bencina: {bencina}")
        automoviles.extend([patente, marca, color, fabricacion, bencina])

    elif opcion == "4":
        listados_general(automoviles, 6)
