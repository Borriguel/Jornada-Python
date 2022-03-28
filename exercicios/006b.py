# aprovar emprestimo para comprar casa. Deve perguntar o valor da casa, salário e quantos anos ele vai pagar.
# calcule o valor da prestação mensal sabendo q ela n pode exceder 30% do salário ou então o empréstimo será negado
valor_da_casa = float(input('Digite o valor da casa. R$'))
salario = float(input('Qual seu salário? R$'))
anos_pagamento = int(input('Deseja pagar em quantos anos?'))

prestacao_mensal = valor_da_casa/(anos_pagamento*12)
if prestacao_mensal > salario*0.3:
    print('Valor da prestação por mês seria de R${:.2f}. Emprestimo negado'.format(prestacao_mensal))
else:
    print('O valor da prestação mensal é R${:.2f} por mês.'.format(prestacao_mensal))
