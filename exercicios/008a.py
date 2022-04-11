# desafio consiste em sortear um número aleatório e o usuário deve advinhar o número

import random

numero_aleatorio = random.randint(1, 11)
chute = tentativas = 0

while chute != numero_aleatorio:
    chute = int(input('Chute um número de 1 a 10 '))
    tentativas += 1
else:
    print('Parabéns! Você acertou o número sorteado {} com {} tentativa(s)'.format(numero_aleatorio, tentativas))
