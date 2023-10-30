class Transporte_Urbano:
    def __init__(self,tipo,modelo,marca):
        self.tipo=tipo
        self.modelo=modelo
        self.marca=marca
    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"modelo: {self.modelo}")
        print(f"marca: {self.marca}")
if __name__=="__main__":    
    j=Transporte_Urbano("ejemplo","uwu","uwu")
    j.mostrar_informacion()