class ContaBancaria:
    def __init__(self, titular):
        self.titular= titular
        self.saldo= saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def ver_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo}")


NomeUser =str(input(f"Digite seu nome: "))
saldo =float(input(f'Digite quantos você tem em conta: '))
Numero =str(input(f"Digite uma das opções\n 1-Depositar \n 2-Sacar \n 3-Ver Saldo \n"))

minha_conta = ContaBancaria(NomeUser)

if Numero == '1':
    valor = float(input("Digite o valor a depositar: "))
    minha_conta.depositar(valor)

elif Numero == '2':
    valor = float(input("Digite o valor a sacar: "))
    minha_conta.sacar(valor)

elif Numero == '3':
    minha_conta.ver_saldo()

else:
    print('Não é uma opção valida')

# Testando a classe ContaBancaria
conta = ContaBancaria('João')
conta.depositar(3000)
conta.sacar(70)
conta.sacar(700)
conta.ver_saldo()