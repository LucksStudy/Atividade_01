class pessoa:
    def __init__(self,nome):
        self.nome=nome
        
    
    def pegar_caneta(self, caneta):
        self.caneta = caneta
        caneta.dono = self.nome

class caneta:
    def __init__(self, cor,):
        self.cor=cor
        self.dono=None

pessoa1 = pessoa("Lucks")
caneta1 = caneta("preto alaranjado")

pessoa1.pegar_caneta(caneta1)
print (caneta1.dono) 
