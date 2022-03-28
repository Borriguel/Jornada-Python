# ler num int qualquer e peça para escolher qual será a base para conversão
num = int(input('Digite um valor inteiro de base decimal '))
print('Qual base deseja que o valor seja convertido, binário, octal ou hexadecimal?')
escolha = int(input('1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))
if escolha == 1:
    print(bin(num))
elif escolha == 2:
    print(oct(num))
elif escolha == 3:
    print(hex(num))
else:
    print('Opção inválida.')
