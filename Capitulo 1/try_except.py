a = 20
b = 0
try: #Intenta hacer algo
    b = a / 0
except ZeroDivisionError as error: #Si el error es zerodivisionerror
    print(error)

print(b)

lista = [10,5,30]

try:
    lista[5] = 30
except IndexError as error:
    print(error)

print("continuo con mi programa")




while False:
    print("""
    1: Ingresar Datos
    2: Mostrar Datos
    3: Salir
    """)

    try:
        opciones = int(input("Indicame el menu: "))
    except ValueError as error:
        opciones = 4
    finally:# Finally siempre se va a ejecutar
        print("Hola") 


    if opciones == 1:
        print("Entro a ingresar datos")
    elif opciones == 2:
        print("Entro a Mostrar datos")
    elif opciones == 3:
        print("Salir del programa")
    elif opciones == 4:
        print("Ingreso no se pueden poner caracteres")

libro = ""
try:
    libro = open("libro.txt","r",encoding= "UTF-8") #abrimos un texto
    #encoding es el uso del texto encoding de nuestro lenguaje
    #"r" representa read existen w write
    archivo = libro.readlines()
    for lineas in archivo:
        print(lineas)

except FileNotFoundError:
    print("No he encontrado el libro")
finally:
    print(f"DEBUG Pase la parte del libro {libro}")

