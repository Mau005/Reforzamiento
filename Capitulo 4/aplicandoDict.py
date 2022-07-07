from boto import config


configuracion = {"Bucle": True, "Usuario": None, "Contraseña": None}
usuariosIngresados = {} #Ingreso de usuarios


while configuracion["Bucle"] == True:
    configuracion["Usuario"] = input("Indicame tu nombre: ")
    configuracion["Contraseña"] = input("Indicame tu contraseña: ")
    
    if len(configuracion["Usuario"])>= 2 and len(configuracion["Contraseña"]) >= 2:
        usuariosIngresados.update({configuracion["Usuario"]:configuracion["Contraseña"]})
    else:
        print("Contraseñas Incorrectas")
    print(usuariosIngresados)
    
    
    if len(usuariosIngresados)>= 3:
        configuracion["Bucle"] = False
        
        
    