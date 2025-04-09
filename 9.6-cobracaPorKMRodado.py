# Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pafar, sabendo qie o carro custa R$: 60,00 por dia r R$0,15 por km rodado

dias = int(input('Quantos dias alugados ?'))
km = float(input('Quantos km rodados ?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
