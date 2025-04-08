# Computador pensa em um numero e jogador tenta adinvinhar

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-')
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens você me venceu!!!')
else:
    print('Ganhei!! Eu pensei no número {} e não no {}'.format(computador, jogador))
