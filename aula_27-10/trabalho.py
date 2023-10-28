class Endereco():
    def __init__(self,rua,cidade ):
        self.rua=rua
        self.cidade=cidade

class Pessoa():
    def __init__(self,nome,endereco ):
        self.nome=nome
        self.endereco = endereco
        print (f'Pessoa {nome} mora no endereço {endereco}')

endereco1 = Endereco ('Avenidade Brasil, 123','Ivaiporã')
pessoa1 = Pessoa(nome="Lucas", endereco=endereco1.cidade) #estipula o local .info
