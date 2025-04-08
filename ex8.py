# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros a milimetros

medida = float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {:.1f}m corresponde a {:.1f}cm e {:.1f}mm'.format(medida, cm, mm))
