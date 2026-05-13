t=str('-=-')
print(t * 20)
print('Vou tentar um número entre 0 e 5. Tente advinhar...')
print(t * 20)
n=int(input('Em que número pensei?'))
from time import sleep
print('PROCESSANDO...')
sleep(2)
from random import randint
r=randint(0,5)
if n == r:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}.'.format(r,n))
