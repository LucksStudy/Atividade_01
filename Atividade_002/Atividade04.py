lista_compras = []

while True:
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Listar itens")
    print("3. Editar item")
    print("4. Excluir item")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        lista_compras.append(item)
        print(f"{item} foi adicionado à lista.")
    elif opcao == "2":
        for item in lista_compras:
            print(item)
    elif opcao == "3":
        indice = int(input("Digite o índice do item a ser editado: "))
        novo_item = input("Digite o novo item: ")
        lista_compras[indice] = novo_item
    elif opcao == "4":
        indice = int(input("Digite o índice do item a ser excluído: "))
        if indice < len(lista_compras):
            item_removido = lista_compras.pop(indice)
            print(f"{item_removido} foi removido da lista.")
        else:
            print("Índice inválido.")
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
