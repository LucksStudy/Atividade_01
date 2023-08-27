sair = "sair"

numero01= float(input (f"digite o primerio número\n"))
operador = input (f"digite o operador\n")
numero02= float(input (f"digite o segundo número\n"))

numero01_float = 0
numero02_float = 0

numero01_float = float(numero01)
numero02_float = float(numero02)

if operador == "+":
    print(f"{numero01_float} + {numero02_float} =",numero01_float + numero02_float)
    
elif operador == "-":
    print(f"{numero01_float} - {numero02_float} =",numero01_float - numero02_float)
elif operador == "*":
    print(f"{numero01_float} * {numero02_float} =",numero01_float * numero02_float)
elif operador == "/":
    print(f"{numero01_float} / {numero02_float} =",numero01_float / numero02_float)
 