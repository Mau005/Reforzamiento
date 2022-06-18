

class Persona:

    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


    def get_nombre(self):
        return self.nombre

    def info(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}"
    
    def set_edad(self,edad_nueva):
        self.edad = edad_nueva




def main():
    lista_persona = []
    lista_persona.append(Persona("Octavio", "Cifuentes", 25))
    lista_persona.append(Persona("Patricio", "Bob esponja", 30))
    lista_persona.append(Persona("El verga", "Larga", 69))
    lista_persona.append("String")
    lista_persona.append(40)
    lista_persona.append(40.5)

    for persona in lista_persona:
        if isinstance(persona,Persona):
            print("Es de la clase persona")
            print(persona.info())
        elif isinstance(persona,str):
            print("Este objeto es un string")
            print(persona)
        elif isinstance(persona,int):
            print("esta persona solo es un entero")
            print(str(persona))
        else:
            print("No esta registrado en ningun dato para recuperarlo")
            print(f"Dato que no se recupero es: {persona}")

        print(persona)

main()