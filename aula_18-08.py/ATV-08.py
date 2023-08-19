dados_cliente = {
    "Nome": "Dieimes",
    "Endereco": "Rua ABC, 123",
    "Telefone": "988179995"
}

print (dados_cliente["Nome"])

dados_cliente ["Cidade"] = "Ivaiporã" # Adicionar item ao Dicionário
print (dados_cliente)

dados_cliente.pop("Telefone") #remover

for indice, valor in dados_cliente.items():  
    print (f"Indice:{indice},valor:{valor}")
    print ("-----------------------------------")
