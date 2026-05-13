print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
p=float(input('Primeiro segmento:'))
s=float(input('Segundo segmento:'))
t=float(input('Terceiro segmento:'))

if p + s > t and s + t > p and p + t > s:
    print('Os segmentos acima PODEM FORMAR um triântulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

