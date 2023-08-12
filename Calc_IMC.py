print ("Bem vindo a calculadora de IMC (indice de Massa Corporal).")
altura = float(input ("digite sua altura!"))
peso = float(input("digite seu peso"))

IMC = peso/(altura*altura)

print (f"Seu IMC é {IMC:.1f}")
if IMC<=18.5:
    print("você esta com magreza")
elif IMC>=18.6 and IMC<=24.9:
    print ("você esta normal")
elif IMC>=25 and IMC<=29.9:
    print ("Você esta com sobrepeso")
elif IMC>=30 and IMC<=34.9:
    print ("Você esta com obesidade I")
elif IMC>=35 and IMC<=39.9:
    print ("Você esta com obesidade II")

else: 
 IMC>=40
 print ("Você esta com obesidade III, Procure um medico!")