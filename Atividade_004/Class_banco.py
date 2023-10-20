from PySimpleGUI import PySimpleGUI as sg

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
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

sg.theme ('black')
layout = [[sg.Text('Theme Browser')],
          [sg.Text('Click a Theme color to see demo window')],
          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]


NomeUser =str(input(f"Digite seu nome: "))
minha_conta = ContaBancaria(NomeUser)

while True:
    alt = str(input(f'Deseja fazer uma alteração?\n1-Sim\n2-Não\n'))

    if alt == '1':
        Numero = str(input(f"Digite uma das opções\n1-Depositar\n2-Sacar\n3-Ver Saldo\n"))

        if Numero == '1':
            valor = float(input("Digite o valor a depositar: "))
            minha_conta.depositar(valor)

        elif Numero == '2':
            valor = float(input("Digite o valor a sacar: "))
            minha_conta.sacar(valor)

        elif Numero == '3':
            minha_conta.ver_saldo()

        else:
            print('----------------------')
            print('Não é uma opção válida')
            print('----------------------')

    elif alt == '2':
        print('--------------------------')
        print('Obrigado pela preferencia!')
        print('--------------------------')
        break
    else:
        print('--------------------------------')
        print('Opção inválida. Tente novamente.')
        print('--------------------------------')

# Testando a classe ContaBancaria
conta = ContaBancaria('Dieimes')
conta.depositar(3000)
conta.sacar(70)
conta.sacar(700)
conta.ver_saldo()