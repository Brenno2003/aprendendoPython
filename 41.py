from datetime import datetime
a = int(input('Qual o seu ano de nascimento: '))
a2 = datetime.today().year
i = a2 - a
print('O atleta tem {} anos'.format(i))
if i <= 9:
    print('MIRIM')
elif 9 < i <= 14:
    print('INFANTIL')
elif 14 < i <= 19:
    print('JUNIOR')
elif 19 < i <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

