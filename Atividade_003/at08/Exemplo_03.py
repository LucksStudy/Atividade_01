def raiz_quadrada(x):
    """
    Essa função recebe um número e devolve sua raiz quadrada
    """
    resultado = x ** (1/2)
    return resultado

# Chamando a função e armazenando o resultado em uma variável
resultado_raiz = raiz_quadrada(25)
print(f"O resultado da raiz quadrada é: {resultado_raiz}")