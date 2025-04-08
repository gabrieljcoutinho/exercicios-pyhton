# Radar eletrônico se o motorista ultrapasaar 80Km/h e a multa vai ser de R$7,00 por cada km acima do limite

velocidade = float(input('Qual é a velocidade do carro?'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
