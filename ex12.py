#Algoritmo que le o preço de um produto e mostra seu novo preço com 5% de desconto

preco = float(input('Qual é o preço do produto? R$: '))
novo = preco - (preco * 5 / 100)
print(' O rpoduto que custava R${:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(
    preco, novo))
