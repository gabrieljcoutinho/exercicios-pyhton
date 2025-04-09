#Faça um progrma que leia um angulo e fale o seno, cosseno e a tangente
from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo qualquer: '))
seno = sin(radians(angulo))
print('O angulo de {} tem SENO de {:.2f}'. format(angulo, seno))

coseno = sin(radians(angulo))
print('O angulo de {} tem COSENO de {:.2f}'. format(angulo, coseno))

tangente = sin(radians(angulo))
print('O angulo de {} tem TANGENTE de {:.2f}'. format(angulo, tangente))
