num = str(input('Digite um número com 4 casas decimais: ')).strip()
print(''' Analisando o número {}
Unidades: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(num, num[3], num[2], num[1], num[0]))

