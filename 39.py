from datetime import datetime

a = int(input('Que o ano voce nasceu: '))
r = datetime.today().year
a2 = r - a
if a2 > 18:
    i = a2 - 18
    aa = r - i
    if i == 1:
        print('Voce tem {} anos, já passou o seu alistamento em {} ano, corra para se alistar'.format(a2, i))
        print('Seu alistamento foi no ano de {}'.format(aa))
    else:
        print('Voce tem {} anos, já passou o seu alistamento em {} anos, corra para se alistar'.format(a2, i))
        print('Seu alistamento foi no ano de {}'.format(aa))
elif a2 < 18:
    i = 18 - a2
    aa = r + i
    if i == 1:
        print('Anida não esta na hora de se alistar, falta {} ano'.format(i))
        print('Seu alistamento será no ano de {}'.format(aa))
    else:
        print('Anida não esta na hora de se alistar, falta {} anos'.format(i))
        print('Seu alistamento será no ano de {}'.format(aa))
else:
    print('Corra para se alistar')
