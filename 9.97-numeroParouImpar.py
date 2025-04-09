# Número par ou ímpar
numero = int(input('Me diga um número qualquer'))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
