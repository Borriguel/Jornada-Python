# ler 2 inteiros e mostrar menu com as opções somar, multiplicar, maior, novos números e sair

escolha = 0

x = int(input('Digite o valor de X '))
y = int(input('Digite o valor de Y '))

while escolha != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos valores\n[5] sair')
    escolha = int(input())
    if escolha == 1:
        print('{} + {} = {}'.format(x, y, x+y))
    elif escolha == 2:
        print('{} x {} = {}'.format(x, y, x*y))
    elif escolha == 3:
        print(max(x, y))
    elif escolha == 4:
        x = int(input('Digite o valor de X '))
        y = int(input('Digite o valor de Y '))
    elif escolha == 5:
        print('fechando')
    else:
        print('Opção inválida')
