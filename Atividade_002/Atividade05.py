numeros = []

for cont in range(5):
    numero= int(input(f"Digite o {cont+1} numero inteiro:"))
    numeros.append(numero)

soma=0
for numero in numeros:
    soma+= numero
    print("\nNúmeros digitados:", numeros)
    print("Soma dos valores:", soma)