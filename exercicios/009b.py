# gerar 5 números aleatórios e colocar em uma tupla, mostrar os números gerados e mostrar o maior e o menor
from random import randint
tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(tupla)
print(f'O maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')
