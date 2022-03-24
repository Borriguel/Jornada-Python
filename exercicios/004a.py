# calcular hipotenusa de um triangulo usando o módulo math.
from math import hypot

b = int(input('digite o valor de um cateto '))
c = int(input('digite o valor do segundo cateto '))

a = hypot(b, c)
print('O valor da hipotenusa vale {}.'.format(a))
