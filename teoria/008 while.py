# loop while executa um conjunto de instruções enquanto a condição for verdadeira
# instrução break para sair do loop mesmo que a condição seja verdadeira
# instrução continue para saltar estado atual de iteração

i = 1
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
else:
    print('i não é mais inferior a 6')
