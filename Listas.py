#iterators
#iterador solo tiene 1 dato asignado pritivo en otros lenguajes


#lista = [20,20,20,20]
#print(f"Mi Lista Principal es: {lista}")
#lista[0] = 30
#lista[1] = 50
#lista.append(40)

#print(f"Mi Lista en el estado actual es: {lista}")
#print(lista[len(lista)])



#lista_estudiantes = ["Elba lazo", "Pepito zaca llama", "Antonio", "Juan"]
#                       0               1                   2        3


#print(lista_estudiantes[len(lista_estudiantes)-1])


#Un programa del clima, que registre muchos grados
# tiene que sacar un promedio
#tiene que indicarme el ultimo ingreso
#el primero ingreso



#grados = [33, 25, 24, 34, 33, 35]
#promedio = 0
#max_grados = grados[len(grados)-1]
#min_grados = grados[0]
#resultado = 0

#sume_grados = 0
#contador = 0
#while contador < len(grados):
#    sume_grados += grados[contador]
#    contador += 1

#resultado = sume_grados / len(grados)



grados = [33, 25, 24, 34, 33, 35]
promedio = 0
max_grados = grados[len(grados)-1]
min_grados = grados[0]
resultado = 0

contador = 0
for grado in grados:
    print(f"Contador posicion: {contador} el valor de grado: {grado}, Mi Dato de contador es: grados[{contador}]")
    resultado += grado
    contador += 1

promedio = resultado / len(grados)



print(f"Grados max: {max_grados}")
print(f"Grados Min: {min_grados}")
print(f"El Promedio: {promedio}")



