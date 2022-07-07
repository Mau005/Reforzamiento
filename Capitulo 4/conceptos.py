#Primitivos
int
bool
float
str

#Funcionalidades del lengue
#list es un array que se auto dimenciona sola, a su vez puede asignar objetos, este
#se puede modificar en toda regla pero es un costo grande para proceso 
#map es un sistema parecido al diccionario pero sirve com uns sitema de mapear un conjunto de objetos
#dict es una tabla hash que funciona a bajo nivel, y puede asignar llaves y valores, llaves unicas
#tuple es una lista inmutable, que no se puede modificar, si se puede copiar, y es sumamente ligera



#Diciconario tiene llave que es unica en el codigo, y asu vez tiene valores
diccionario = {"Juan": "Antonio", 23: "Roberto", True: "Mama este presa"}
diccionario["Juan"] #Retorna Antoniio
diccionario[23] #retornar Roberto
diccionario[True] # retorna mama esta presa

for elementos in diccionario:
    if elementos == "Juan":
        print(f"Encontre a {elementos} y su valor es {diccionario[elementos]}")
    
    
#buscar elementos en el diccionario
#elementos pasa a valer un valor del diccionario
#el primer valor recorrido son las keys
#puedes iterar varias formas el sistema


#nueva = [ [10,45,60,45], [10,45,60,45]]

#nueva = ["Hola Incap", "Office 365", "Hola Mundo"]
#len(3 elementos)
#elemento 1 - 10 caracteres
#elementos 2 - 10 caracteres
#elementos 3 9 caracateres
    #nueva[0]

#indice = 0
#for elementos in nueva:
#    if elementos == "Hola Mundo":
#        print("Lo Encontre!! Biene en el contador: ", indice)
#    indice +=1
