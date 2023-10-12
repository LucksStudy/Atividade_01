class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso.')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente.')

    def ver_saldo(self):
        print(f'O saldo atual é R${self.saldo}.')

# Testando a classe ContaBancaria
conta = ContaBancaria('João')
conta.depositar(1500)
conta.sacar(500)
conta.sacar(700)
conta.ver_saldo()