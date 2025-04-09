# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
real = float(input('Quanto dinheiro você tem na carteira? R$: '))
dolar = real / 5.55
euro = real / 0.92
print('Com R$ {:.2f} você pode comprar US$ {:.2f} e EUR {:.2f} '.format(real, dolar, euro))
