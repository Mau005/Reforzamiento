import os
datos = []

variable_1 = """
Configuracion
usuario = Mau
password = ICLcreyo
correo = mpino1701@gmail.com
"""
#variable_4 = input("Devuelvo una cadena de texto: ")


lineas = variable_1.split("\n") # El string se vuelve lista y separa por todos los saltos de linea

for linea in lineas:
    contenido = linea.replace(" ", "")
    contenido = contenido.split("=")
    if contenido[0] == "usuario":
        print(f"entonces el usuarion es: {contenido[1]}")
        datos.append(contenido[1])
    elif contenido[0] == "password":
        print(f"Entonces el password es: {contenido[1]}")
        datos.append(contenido[1])
    elif contenido[0] == "correo":
        print(f"Entonces el correo es : {contenido[1]}")
        datos.append(contenido[1])


print(datos)



formato = "https://"

webs = """
www.ainhosoft.cl
www.google.cl
www.netacad.net
www.losamigosdetuhermana.com
"""


for lineas in webs.split("\n"):
    if len(lineas) >= 2:
        print(formato+lineas+"/")



archivo = open("archivo2.txt", "w")
archivo.write(variable_1)