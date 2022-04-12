# desafio pa, ler o primeiro termo, a razão e mostrar os 10 primeiros termos da pa

a1 = int(input('Digite o primeiro termo da P.A '))
r = int(input('Digite a razão '))
n = 1
escolha = 0

while escolha != 2:
    escolha = int(input('Deseja ver 10 termos consecutivos da P.A?\n[1] - Sim \n[2] - Não \n'))
    if escolha == 1:
        for c in range(1, 11):
            print('{}'.format(a1 + n*r), end=', ')
            n += 1
        print('(...)')
    elif escolha == 2:
        print('Fechando')
