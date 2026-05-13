s=float(input('Qual o valor do salário do funcionário? R$' ))
if s <= 1250:
    ns = s * 1.15
else:
    ns = s * 1.1

print('Quem ganhava R${:.2f}, com o aumento, passa a garnhar R$ {:.2f}.'.format(s, ns))