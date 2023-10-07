class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mensagem(self):
        print (f"O nome é {self.nome} e minha idade é {self.idade}.")


nome=input(str("digite seu nome"))
idade=input(str("digite sua idade"))

aluno2= Estudante(nome,idade)
aluno2.mensagem()
