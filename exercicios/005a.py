# ler um nome e mostrar em maísculo, minúsculo, quantas letras sem mostrar espaços e quantas letras tem o primeiro nome
nome = input('digite seu nome')
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
primeiro_nome = nome.split()
print('{} tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))
