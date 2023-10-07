class Carro:
    pneus = 4 #atributo de classe

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 =Carro("Ford","Fiesta")
carro2 =Carro("Honda","Civic")

print (carro1.pneus)
print (carro2.pneus)

print (Carro.pneus)

class Turma:
    def __init__(self, nome, sobrenome):
        self.nome=nome
        self.sobrenome =sobrenome

    def texto(self):
        print (f"O meu nome é {self.nome} e meu sobrenome é {self.sobrenome}")

aluno1 = Turma("Lucas","Dias")

print(aluno1.nome)
print(aluno1.sobrenome)

aluno1.texto()

class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mensagem(self):
        print (f"O nome é {self.nome} e minha idade é {self.idade}.")


nome=input(str("digite seu nome"))
idade=input("digite sua idade")

aluno2= Estudante(nome,idade)
aluno2.mensagem()
