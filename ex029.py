v=float(input('Qual é a velocidade do carro em km/h?'))
if v > 80:

    print('MULTADO! Você excedeu o limiter permitido, que é 80 km/h.')
    print('Você deve pagar uma multa de R${:.2f}.'.format((v-80)*7))

print('Tenha um bom dia! Dirija com segurança!')
