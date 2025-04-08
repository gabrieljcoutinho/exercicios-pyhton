# Faça um programa que leia a largura e a altura de uma parede
# em mestros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# pinta uma áre de 2m quadrados

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimesão de {}x{} e sua área é de {}m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {} L de tinta'.format(tinta))
