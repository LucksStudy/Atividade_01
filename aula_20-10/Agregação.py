class estudante:
    def __init__(self, nome):
        self.nome = nome

class turma:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []
    
    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

joao = estudante("João")
maria = estudante("Maria")

turmaA = turma ("Turma A")
turmaA.adicionar_estudante(joao)
turmaA.adicionar_estudante(maria)

print (turmaA)