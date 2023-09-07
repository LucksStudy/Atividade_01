alunos = {}

for i in range(3):
 nome = input(f"Digite o nome do {i + 1}º aluno: ")
 nota = float(input(f"Digite a nota de {nome}: "))
 alunos[nome] = nota 

soma_notas = 0
for nota in alunos.values():
   soma_notas += nota 

media = soma_notas / 3 

print("\nDados dos Alunos:")
for nome, nota in alunos.items():
   print(f"{nome}: {nota}")
print("\nMédia das Notas:", media)#