

#if [exprecion depregunta retornara True o False]:
#    [contenido del condicional]

#pepitozacallama = "Oka"
#if condicion == 1 and condicion2 == "Antonio" or pepitozacallama == "Oka":
#    print("Entro en la condicion")

#while [Condicion verdadera para funcioanr, mientras esta sea verdadera se ejecutara]
#condicion = 1
#condicion2 = "Antonio"
#pepitozacallama = "Oka"
#contador = 0
#while condicion == 1 and condicion2 == "Antonio" or pepitozacallama == "Oka":
#    print("Entro en el bucle")
#    contador +=1
#    if contador >= 1000:
#        pepitozacallama = "no"
#print("Estoy fuera del bucle")

#0 == False
#1 == True
#"True" == True : True
#"False" == False : True

condicion1 = True
condicion2 = True
while condicion1 == True and condicion2 == True:
    print("""
    Menu Programa de COndiciones de bucles
    1: Cambiar condicion 1
    2: Cambiar condicion 2

    """)
    opcion =  int(input("Dame la Opcion: "))
    if opcion == 1:
        condicion1_cambiar = int(input("Dime 1 si es verdadero dime 0 si es falso: "))
        condicion1 = condicion1_cambiar
    elif opcion == 2:
        condicion2_cambiar = int(input("Dime 1 si es verdadero dime 0 si es falso: "))
        condicion2 = condicion2_cambiar

print("Estoy fura del bucle")


