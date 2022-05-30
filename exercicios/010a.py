# Leia 5 valores inteiros e guarde-os em uma lista, no final mostre qual foi o maior, o menor e suas posições

lista = []
for contador in range(1, 6):
    valor = int(input(f'Digite o {contador}º valor: '))
    lista.append(valor)
print(f'O maior valor é {max(lista)} no índice ', end='')
for indice, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{indice}...', end='')
print()
print(f'O menor valor é {min(lista)} no índice ', end='')
for indice, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{indice}...', end='')
