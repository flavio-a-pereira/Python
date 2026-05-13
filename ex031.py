d=float(input('Qual é a distancia da sua viagem?'))
print('Você está prestes a realizar uma viagem de {} km.'.format(d))
if d<= 200:
        print('E o preço da sua passagem será de R$ {:.2f}.'.format(d*0.5))
else:
        print('E o preço da sua passagem será de R$ {:.2f}.'.format(d*0.45))

# utilizando operador ternário ou if simplificado
preço = d * 0.5 if d <=200 else d * 0.45
print('Nesta linha, utilizando o if simplificado, o resultado seria também de R$ {}'.format(preço))

