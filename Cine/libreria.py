import numpy as np

asientos = np.zeros(30, dtype=int)# crea una matriz de 30 elementos


def MostrarAsientos():
    for elementos in range(len(asientos)):
            print(f"[ID: {elementos+1} Estado {asientos[elementos]}]", end= " ")

def AsignarAsiento(numeroDeAsiento):
    #todo array su indice inicial es 0
    #si quiero el asiento 1 el indice del array debe ser asientos[0]
    if asientos[numeroDeAsiento - 1] == 0:
        asientos[numeroDeAsiento - 1] = 1
        return True, "Se a comprado el asiento"
    else:
        return False, "Asiento ocupado, pregunte por otro FDP"
    
def FormatoFecha(año,mes,dia):
    formato = f"{año}-0{dia}-0{mes}"
    formato2 = f"{año}-{dia}-{mes}"
    if int(mes)>= 1 and int(mes)<=9 and int(dia)>= 1 and int(dia)<=9:
        return formato
    else:
        return formato2

class Persona():
    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def info(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}, Edad: {self.edad}"
        
        