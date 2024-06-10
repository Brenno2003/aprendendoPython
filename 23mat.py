num = int(input('Valor com 4 digitos: '))
un = num // 1 % 10
dez = (num // 10) % 10
cent = (num // 100) % 10
mil = (num // 1000) % 10
print('''Analisando {}
Unidade: {}
Dezena: {:.0f}
Cetena: {:.0f}
Milhar: {:.0f} '''.format(num, un, dez, cent, mil))




