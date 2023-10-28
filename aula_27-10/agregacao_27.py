class Autor:
    def __init__(self,nome):
        self.nome=nome

class livro:
    def __init__(self,autor,nome):
        self.nome = nome
        self.autor =autor
        print (f'O livro {nome} foi escrito por {autor} ')

    
livro1= livro ('frank castle','formas de fazer amor')
autor1= Autor ('frank castle')

