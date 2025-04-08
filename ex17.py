'''faça um program que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa'''

from math import hypot
ca = float(input('Comprimento do cateto oposto: '))
co = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
