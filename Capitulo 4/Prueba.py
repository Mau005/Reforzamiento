#GUI Menu con las b bonito bueno y barato
# opcion de salida
#confirmacion de datos
#Posibilidad de funciones

# Sistema de datos donde se encuentren usuarios con sus contraseñas y sus datos personales °Diccionario
# la aplicacion se puede iniciar session por cada uno de los usuarios if
# y puede asignar informacion en un libro, donde podra tener notas diccionarioo
# en estas notas quedara registrado por cada usuario por este

#Ale


usuarios = {}

def RegistrarUsuarios(key,value):
    """Methodo que registra los datos

    Args:
        key (string): El nombre de usuario que registra
        value (dict): diccionario con los valores de {"contraseña": None, "edad": None, "nombre": None}
    """
    #"nombre":{"contraseña": None, "edad": None, "nombre": None}
    usuarios.update({key:value})
    
def SolicitarDatos(key,tipoKey):
    """Methodo que recoje los datos de un usuario

    Args:
        key (string): nombre del usuario
        tipoKey (string): nombre del atributo a solicitar

    Returns:
        datos: dependiendo de lo que soliciten
    """
    try:
        return usuarios[key][tipoKey]
    except KeyError as error:
        print(f"Usuario {key} no esta en la BD")
        return None

def VerificarInformacion(usuario,contraseña):
    contraseñaGuardada = SolicitarDatos(usuario,"contraseña")
    if contraseña == contraseñaGuardada:
        return True
    return False

def hola():
    print("hola")

def main():
    enMovimiento = True
    while enMovimiento:
        
        usuario = input("Dame tu Nombre de Usuario: ")
        contraseña = input("Dame Tu Contraseña: ")
        
        if VerificarInformacion(usuario, contraseña):
            print("Inicio Seccion")
        else:
            while True:
                opcion = input("Desea crear un usuario? y/n")
                if "y" in opcion.lower():
                    pass
                elif "n" in opcion.lower():
                    enMovimiento =False
                    break
                else:
                    print("Indica el caracter correcto CTM")
            
main()
        
        
        