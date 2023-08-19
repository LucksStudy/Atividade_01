lista1 = ["Dieimes", "Nunes", "Souza", "Caio","Luana"]
print (type(lista1))
print(len(lista1))  #imprimir qt itens lista
print(lista1[4])

lista2 = lista1*2

print (lista2)

lista1.append ("amanda") #adicionar elemento na lista exemplo um novo nome!
print (lista1)

lista1.remove("Caio") #remover elemento da lista
print (lista1)

lista1.pop(3) #Remover elemento da lista também
print (lista1)

for listageral in lista1:
    print (listageral)