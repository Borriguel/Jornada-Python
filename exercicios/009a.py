# criar tabela do brasileirão, mostrar os 5 primeiros, 4 últimos e posição da chapecoense na tabela
tabela_brasileiro = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athlético-PR', 'São Paulo', 'Internacional',\
                    'Corinthians', 'Fortaliza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',\
                    'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
print('Os 5 primeiros')
print(tabela_brasileiro[:5])
print('Os 4 útimos')
print(tabela_brasileiro[-4:])
print('Tabela em ordem alfabética')
print(sorted(tabela_brasileiro))
print('Posição da Chapecoense')
print(tabela_brasileiro.index('Chapecoense') + 1)
