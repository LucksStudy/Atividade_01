class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

    def designar_professor(self, professor):
        self.professor = professor

    def obter_professor(self):
        return self.professor.nome if self.professor else "Nenhum professor designado."


class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def lecionar_curso(self, curso):
        self.cursos.append(curso)

    def listar_cursos(self):
        return [curso.nome for curso in self.cursos]


if __name__ == "__main__":
    curso1 = Curso("Python")
    curso2 = Curso("Analise de porjeto")
    professor1 = Professor("Dieimes")
    professor2 = Professor("Michael")
    
    curso1.designar_professor(professor1)
    curso2.designar_professor(professor2)
  
    professor1.lecionar_curso(curso1)
    professor2.lecionar_curso(curso2)

    print(f"{professor1.nome} leciona: {professor1.listar_cursos()}")
    print(f"{professor2.nome} leciona: {professor2.listar_cursos()}")

    print(f"O professor do curso de {curso1.nome} é: {curso1.obter_professor()}")





