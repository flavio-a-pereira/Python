import math
co=float(input('O cumprimento do cateto oposto é:'))
ca=float(input('O cumprimento do cateto adjacente é:'))
h=math.sqrt((co)**2+(ca)**2)
print('A hipotenusa vai medir {:.2f}.'.format(h))

# outra forma com a função math.hypot

from math import hypot
co=float(input('Cateto oposto:'))
ca=float(input('Cateto adjacente:'))
h=math.hypot(co,ca)
print('Por esse método, o valor da hipotenusa também é {:.2f}.'.format(h))
