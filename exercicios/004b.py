# leia um ângulo e retorne o valor do seno, cosseno e tang desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input('digite o valor de um ângulo em º. '))
print('Sen{0}º: {1:.2f}, Cos{0}º: {2:.2f} e Tag{0}º: {3:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
