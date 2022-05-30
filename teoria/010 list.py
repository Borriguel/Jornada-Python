# List são variáveis compostas MUTÁVEIS
numeros = [1, 2, 3, 4, 6]
numeros[4] = 5
numeros.append(6)
print(numeros)
numeros.pop(5)
print(numeros)
print(f'A lista tem {len(numeros)} elementos')
