s = float(input('Qual o seu salaro: R$ '))
if s > 1250:
    a1 = s * 1.1
    print('O seu salario atual será de {:.2f}'.format(a1))
if s <= 1250:
    a2 = s * 1.15
    print('O salario atual sera de {:.2f}'.format(a2))
