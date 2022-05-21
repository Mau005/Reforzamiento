
variable_nueva = None
tupla_es = (10,45,60,30)
lista_es = [10,45,60,30]

variable_nueva = list(tupla_es) #asignamos la tupla a lista
variable_nueva[0] = 12 #editamos la lista nuev a
tupla_es = tuple(variable_nueva) #a signamos la lista a tupla

x = []
for elementos in tupla_es:
    x.append(elementos)

print(x)


#tuple es una lista que no se puede modificar
#list es una lista que puede modificarse
#Terminos de proceso la tuple es mas ligera que la lista
#tiene menos datos y pesa menos en el programa







