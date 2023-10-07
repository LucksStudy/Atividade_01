class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao= ano_publicacao

    def descricao(self):
        print (f"Titulo:{self.titulo}\n Autor:{self.autor}\n Ano de publicação:{self.ano_publicacao}")

lib= Livro("Caneta Azul","Manoel Gomes","2020")
lib2= Livro("Precisamos falar sobre Tony","GayTony","2016")

print (lib.titulo)
print (lib.autor)
print(lib.ano_publicacao)

lib.descricao()


print (lib2.titulo)
print (lib2.autor)
print(lib2.ano_publicacao)

lib2.descricao()