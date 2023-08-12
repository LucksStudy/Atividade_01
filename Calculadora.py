sair = "sair"

numero01= input ("  digite o primerio numero")
numero02= input ("  digite o segndo numero")
operador = input ("  digite o operador")

numero01_float = 0
numero02_float = 0

numero01_float = float(numero01)
numero02_float = float(numero02)

if operador == "+":
    print(f"{numero01_float} + {numero02_float} =",numero02_float + numero01_float)