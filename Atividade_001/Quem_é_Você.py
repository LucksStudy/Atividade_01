nome = str(input("qual seu nome?"))
sobre = str(input("qual seu sobrenome?"))
altura = float(input ("qual sua altura?"))
peso = float(input ("qual seu peso?"))
idade = int(input("qual sua idade?"))


print("informações pessoais!")
print ("Nome Completo:",nome,sobre)
print("Idade:",idade,"anos")
print ("Altura:",altura,"metros")
print ("Peso:",peso, "KG")
if idade>18:
    print ("Você é maior de idade") 
else:
    print("Você é menor de idade")
