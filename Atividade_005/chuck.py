class Cabeça:
    def __init__(self, cor_olhos, cor_cabelo):
        self.cor_olhos = cor_olhos
        self.cor_cabelo = cor_cabelo

    def __del__(self):
        print("Cabeça destruída.")

class Boneco:
    def __init__(self, nome, cor_olhos, cor_cabelo):
        self.nome = nome
        self.cabeca = Cabeça(cor_olhos, cor_cabelo)

    def __del__(self):
        print(f"Boneco {self.nome} destruído.")

    def destruir_boneco(self):
        del self

if __name__ == "__main__":

    boneco1 = Boneco("chuck", "azul", "castanho")
    print(f"A cabeça do boneco {boneco1.nome} tem olhos {boneco1.cabeca.cor_olhos} e cabelo {boneco1.cabeca.cor_cabelo}.")

    boneco1.destruir_boneco()

    try:
        print(f"A cabeça do boneco {boneco1.nome} tem olhos {boneco1.cabeca.cor_olhos} e cabelo {boneco1.cabeca.cor_cabelo}.")
    except AttributeError as e:
        print(f"Erro: {e}")