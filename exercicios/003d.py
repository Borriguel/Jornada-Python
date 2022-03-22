# ler um valor em metros e converter para cm e mm
valor = float(input('Digite um valor'))
valorcm = valor*100
valormm = valor*1000
print('O valor em {} m corresponde a {:.0f} cm e {:.0f} mm'.format(valor, valorcm, valormm))
