import datetime
a=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if a==0:
    na=int(datetime.date.today().year)
else:
    na=a

if na % 4 == 0 and na % 100 != 0:
    print('O ano {} é bissexto'.format(na))
elif na % 4 == 0 and na % 100 ==0 and na % 400 ==0:
        print('O ano {} é bissexto'.format(na))
else:
    print('O ano {} não é bissexto'.format(na))

# outra forma mais simples

if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 ==0:
    print('O ano {} é bissexto'.format(a))
else:
    print('O ano {} não é bissexto'.format(a))