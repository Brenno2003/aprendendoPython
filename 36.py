vc = float(input('Qual o valor da casa: R$ '))
s = float(input('Qual o seu salario: R$ '))
a = int(input('Em quantos anos voce quer pagar: '))
p = vc/(a*12)
ps = s*0.3
if p > ps:
    print('Não pode financiar essa casa')
else:
    print('O valor de cada pacela será de R$ {:.2f}'.format(p))


