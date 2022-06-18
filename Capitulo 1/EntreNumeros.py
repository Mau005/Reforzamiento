#programa que identifica si el numero es entre 0 y 30
#identifica a que grupo de numero corresponde si es mayores 1 hasta 10
#del 10 asta 20
#del 20 hasta el 30
# sino indicar que el numero no calsa a ninguno de ellos


x = int(input("Dame un numero: "))

if x >= 0 and x < 30:
    if x >= 0 and x < 10:
        print("El numero pertenece al grupo de los -10")
    elif x >= 10 and x < 20:
        print("El Numero pertenece a los grupo de  los -20")
    elif x >= 20 and x <= 30:
        print("El Numero esta en los grupos de los =a -30")
        
else:
    print("Digito mal el numero")
