# Jogo de par ou impar, só acaba com a derrota
import random

print('~' * 30)
print('É hora do duelo!!!')
print('~' * 30)
vitorias = 0
while True:
    numero = int(input('Diga um valor maior ou igual a 0: '))
    escolha = str(input('Par ou Ímpar? [P/I] '))
    numero_maquina = random.randint(0, 11)
    valor = numero + numero_maquina
    print('-' * 30)
    if escolha.upper() == 'I':
        if valor % 2 != 0:
            print(f'Você venceu a rodada! Você jogou {numero} e a máquina {numero_maquina} total {valor} Ímpar')
            print('-' * 30)
            vitorias += 1
        else:
            print(f'Você perdeu a rodada! Você jogou {numero} e a máquina {numero_maquina} total {valor} Par')
            break
    if escolha.upper() == 'P':
        if valor % 2 == 0:
            print(f'Você venceu a rodada! Você jogou {numero} e a máquina {numero_maquina} total {valor} Par')
            print('-' * 30)
            vitorias += 1
        else:
            print(f'Você perdeu a rodada! Você jogou {numero} e a máquina {numero_maquina} total {valor} Ímpar')
            break
print('=-' * 30)
print(f'Fim de jogo, você venceu {vitorias}x')
