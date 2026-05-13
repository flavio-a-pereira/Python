p=int(input('Primeiro valor:'))
s=int(input('Segundo valor:'))
t=int(input('Terceiro valor:'))
menor = p
maior = s
if s < menor:
    menor = s
    maior = p
else:
    menor =p
    maior = s

if t < menor:
    menor = t
else:
    menor = menor
    
if t > maior:
    maior = t
else:
    maior = maior

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
