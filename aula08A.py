# importação de todas as funcionalidades

import math
num=int(input('Digite um número:'))
raiz=math.sqrt(num)
print('A raiz de {} é {:.2f}.'.format(num, raiz))
print('Arredondadando para cima será {}'.format(math.ceil(raiz)))
print('E para baixo: {}'.format(math.floor(raiz)))

# importando só a funcionalidades específicas

from math import sqrt, floor
n = int(input('Digite outro número:'))
raiz = sqrt(n)
print('A raiz de {} é {:.2f}'.format(n, raiz))
print('Arredondando para baixo: {:.2f}.'.format(floor(raiz)))

# importando a biblioteca random

import random
n1 = random.random()
n2 = random.randint(1,10)
print(n1,n2)



