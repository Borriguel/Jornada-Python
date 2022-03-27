# python possui 2 formas de realizar condicionais if sendo uma padrão e outra simplificada semelhante ao if ternário
# como outras linguagens

#    if condicao:
#       realiza alguma ação caso condição = True
#   else:
#       realiza a ação caso condição = False

if 2 > 1:
    print(True)

dinheiro = int(input('quanto tem na sua carteira?'))
print('rico'if dinheiro>=10 else 'pobre')
