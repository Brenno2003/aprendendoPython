v = float(input('Qual foi a velocidade do carro, em Km: '))
vm = v - 80
if v <= 80:
    print('Está em uma velocidade permitida')
else:
    s = vm * 7
    print('A tera que pagar o valor de R$ {:.2f}'.format(s))
print('Tenha um bom dia diriga com segurança')

