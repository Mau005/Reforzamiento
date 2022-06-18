#Los dic son tablas hash son sumamente rapidas
#usan una key y entregan un valor
#sintaxis dict = {key:valor, key:valor....}


usuarios = {"Mau": 27, "Pepito": 45, "Juan":77, 66:"Juan"}
print(usuarios["Pepito"])
print(usuarios[66])

#for llaves in usuarios:
#    print(f"Mi llave es: {llaves} : EL valor es: {usuarios[llaves]}")

usuarios["Mau"] = 45 #cambiamos un valor de las llaves
print(usuarios)

usuarios.update(hola = "25")
#usuarios.update(4 = "25") # no se pueden asignar int como llaves de esta forma
usuarios.update({1 : "25"})# si se peude asignar un entero como llave enviandolo ocmo dict
usuarios.update({"hola2" : 25})
print(usuarios)



