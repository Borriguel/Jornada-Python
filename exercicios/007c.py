# calcular soma de todos os números ímpares múltiplos de três de intervalo 1 até 500
soma = 0
contador = 0
for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        soma += num
        contador += 1
print('O valor da soma dos {} termos é {}'.format(contador, soma))
