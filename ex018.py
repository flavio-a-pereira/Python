import math
a=float(input('Digite o valor de um ângulo:'))
print('O seno de {} é {:.2f}.'.format(a,math.sin(math.radians(a))))
print('Já o coseno é {:.2f}.'.format(math.cos(math.radians(a))))
print('E a tangente é {:.2f}.'.format(math.tan(math.radians(a))))
