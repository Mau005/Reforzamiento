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


automoviles = ["abcd12", 2-5-2020, "cambio de aceite",
             "hjfd02",10-4-2019,"lavado de motor",
             "dfgl03",29-8-2020,"Manrencion general"]

mantenimientos = ["abcd12", 2-5-2020, "cambio de aceite",
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
            marca = input("Dame la marca: ")

            if marca == "":
                os.system("cls")
                print("No puede quedar la marcar sin asignar: ")
            else:
                break

        while True:
            color = input("Dame el Color: ")

            if color == "":
                os.system("cls")
                print("No puede quedar el Color sin asignar: ")
            else:
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

            bencina = input("Indiqueme el tipo de combustible: ")
            #b, d, e, h 
            if bencina == "b" or bencina == "d" or bencina == "e" or bencina == "h":
                break
            else:
                os.system("cls")
                print("Indique bien el tipo de combustible con B-D-E-H en minisculas")

        print(f"Se ha registrado el vehiculo: Patente: {patente}, marca: {marca}, color: {color}, Año Fabricacion: {fabricacion}, Bencina: {bencina}")
        automoviles.extend([patente, marca, color, fabricacion, bencina])

    elif opcion == "2":
        #Registro Mantenimiento: Deberá en primera instancia solicitar la Patente del vehículo, 
        #luego verifica que el vehículo se encuentre registrado en el sistema, una vez validado se le 
        #solicitará ingresar la fecha y las observaciones para que el mecánico pueda revisar, y lo almacenará en la 
        #LISTA de registros. 
        while True:
            buscar = input("Dame la patente: ")

            aux = 0
            for automovil in automoviles:
                if automovil == buscar:
                    # = "dd-mm-aaaa"
                    print("El vehiculo si se encuentra: ")
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
                            print("Error de datos, ingrese nuevamente la fecha")

                    observaciones = input("Dame la observacion correspondiente: ")
                    mantenimientos.extend([automovil, formato_fecha,  observaciones])
                    print(f"Se ha ingresado el mantenimiento de: {automovil}, {formato_fecha}, Observaciones: {observaciones}")
                    input("Precione una tecla para continuar ...")
                    break
            
            break
    elif opcion == "3":
        buscar = input("Dame la patente: ")
        contador = 0
        encontrado = False
        for vehiculo in automoviles:
            if vehiculo == buscar:
                print("""
                patente: {}
                Modelo: {}
                Color: {}
                Año: {}
                Combustible: {}
                """.format(automoviles[contador], automoviles[contador +1], automoviles[contador + 2], automoviles[contador + 3], automoviles[contador + 4]))
                encontrado = True
            contador += 1
        if not encontrado:
            print("No se ha encontrado ningun vehiculo")
        input("Precione una tecla para continuar ...")

    elif opcion == "4":
            #4.	Listado General de Autos atendidos (Mantenciones).
            cantidad_mantenimientos = int(len(mantenimientos) / 3)- 1 #Si cada 3 elementos en 1 lista corresponde a un vehiculo, lo devidido por la longitud de la lista para determinar cuantos vehiculos tengo, -1 por que buscaremos indices de una lista
            
            for vehiculo in range(0,cantidad_mantenimientos):
                posicion_actual = cantidad_mantenimientos* vehiculo
                print("""
                patente: {}
                Fecha Ingreso: {}
                Observaciones: {}
                """.format(mantenimientos[posicion_actual], mantenimientos[posicion_actual +1], mantenimientos[posicion_actual + 2]))
            input("Precione una tecla para continuar ...")
            os.system("cls")
    elif opcion == "5":
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
                print(formato_fecha)
                contador = 0
                for fecha in mantenimientos:

                    if fecha == formato_fecha:
                        print("""
                        patente: {}
                        Fecha Ingreso: {}
                        Observaciones: {}
                        """.format(mantenimientos[contador - 1], mantenimientos[contador], mantenimientos[contador + 1]))
                    contador += 1 
                input("Precione una tecla para continuar ...")
                os.system("cls")
                break
                
            except ValueError:
                print("Error de datos, ingrese nuevamente la fecha")
    elif opcion == "6":
        buscar = input("Indiqueme la observacion: ")

        input("Precione una tecla para continuar ...")
        os.system("cls")
    elif opcion == "7":
        print("Cerrando Secion")
        break






        


                    


