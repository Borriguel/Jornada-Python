# desafio ler vários números inteiros, o programa só vai parar quando digitar 999, no final somar os inteiros e
# quantos inteiros foram digitados.

soma = inteiros = 0
while True:
    entrada = int(input('Digite valor inteiro: '))
    if entrada == 999:
        break
    soma += entrada
    inteiros += 1
print(f'A soma dos {inteiros} inteiros foi {soma}')
