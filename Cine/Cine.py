"""
    Crear un programa que permita vender entradas para el cine.
Hay una única función a las 20:30  la película de terror es   |Profe Pro
"Se que no estudiaste para el examen" |Profe Pro

El cine dispone de 30 asientos y tiene precios para 
tercera edad $1500, adulto $5000 y niños $2000.

Las opciones del menú son:

1. Vender entrada. 

2. Ver asientos (muestra todos los asientos libres y ocupados X)

3. Reporte de ventas  por fecha

4. Reporte de ventas mensual

5. Salir.| menu echo profe pro
"""

import os
import Cine.libreria as lib
import datetime

precios = {"1": 1500, "2": 5000, "3":2000}
vendidos = {str(datetime.date.today()):0}


enMovimiento = True #El siclo de ejecucion de toda la aplicacion

while enMovimiento:
    print("""
Las opciones del menú son:
1. Vender entrada. 
2. Ver asientos (muestra todos los asientos libres y ocupados X)
3. Reporte de ventas  por fecha
4. Reporte de ventas mensual
5. Salir.""")

    opciones = input("Dame la Opcion: ")
    
    if opciones == "1":
        while True:
            print(f"[1] Entrada Adulto Mayor: {precios['1']}")
            print(f"[2] Entrada Adulto: {precios['2']}")
            print(f"[3] Entrada Niños: {precios['3']}")
            entrada = input("Indique que entrada necesita: ")
            if entrada == "1" or entrada == "2" or entrada == "3":
                lib.MostrarAsientos()
                asiento = input("Indiqueme el asiento: ")
                compra = lib.AsignarAsiento(int(asiento))
                if compra[0]:
                    print(compra[1])
                    vendidos[str(datetime.date.today())] += precios[entrada]
                else:
                    print(compra[1])                
                volver = input("Desea comprar otra entrada? y/n o s/n:")
                if "y" in volver.lower() or "s" in volver.lower():
                    continue
                else:
                    break
                
    elif opciones == "2":
        lib.MostrarAsientos()
        input("Precione para continuar.. ")
    elif opciones == "3":
        mes = input("Mes: ")
        año = input("Año: ")
        dia = input("dia: ")
        try:
            print(f'Ventas del dia: {vendidos[lib.FormatoFecha(año,mes,dia)]}')
        except KeyError as error:
            print("Esta fecha no tiene datos registrados")
        input("Precione para continuar")
    elif opciones == "4":
        print(vendidos)
    elif opciones == "5":
        enMovimiento = False
    else:
        print("Ha escrito mal el menu Vuelva a intentarlo... ")
        input("Precione para continuar...")
        os.system("cls")