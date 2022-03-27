# calcular a média
nota1 = int(input('quanto tirou na primeira prova? '))
nota2 = int(input('e na segunda? '))
nota3 = int(input('agora pra fechar com chave de ouro me diz q tirou um 100 '))

if (nota1+nota2+nota3)/3 >= 50:
    print('APROVADO LEK')
if (nota1+nota2+nota3)/3 < 50:
    print('aí n po, vai apanhar agr')
if (nota1+nota2+nota3)/3 == 100:
    print('NERDOLA!')
