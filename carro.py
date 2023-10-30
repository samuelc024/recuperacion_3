from transporte_urbano import Transporte_Urbano
class Carro(Transporte_Urbano):
    def __init__(self,carro_particular,modelo,marca):
        self.tipo=carro_particular
        self.modelo=modelo
        self.marca=marca

