# estruturas condicionais

# estrutura simples
nome=str(input('Qual é o seu nome?'))
if nome == 'Flavio':
    print('Eu te conheço!')
print('Bom dia, {}'.format(nome))

#estrutura composta, com if e else

nome=str(input('Qual é o seu nome?'))
if nome == 'Flavio':
    print('Eu te conheço')
else:
    print('Eu não te conheço!')
print('Bom dia, {}.'.format(nome))

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m>= 6.0:
    print('Sua média foi boa. Parabens!')
else:
    print('Sua média foi ruim!')
    print('Estude mais...')

# if simplificado

print('PARABÉNS' if m>= 6 else 'ESTUDE MAIS...')
