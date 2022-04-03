# ler 6 números inteiros e mostrar a soma apenas dos que forem pares.
soma = 0
for x in range(1, 7):
    num = int(input('digite o {}º valor '.format(x)))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares é {}'.format(soma))
