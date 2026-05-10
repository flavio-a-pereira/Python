from math import trunc
n=float(input('Digite um número:'))
print('O número {} tem a parte é inteira {}.'.format(n,trunc(n)))

# outro modo

n=float(input('Digite outro número:'))
print('Nesse caso, o número digitado foi {} e sua parte inteira é {}.'.format(n,int(n)))
