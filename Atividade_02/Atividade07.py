import numpy as np

diemes_matris = np.array ([[3, 4, 1],
                           [3, 2, 1]]) 

soma = 0 

for linha in diemes_matris:
 for elemento in linha:
   soma += elemento 

print("Matriz:")
print(diemes_matris)
print("\nSoma dos elementos:", soma)