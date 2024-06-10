k = float(input('Qual a distancia da sua viagem: '))
print('Você vai começar uma viagem de {:.2f} Km'.format(k))
if k <= 200:
    d1 = k * 0.50
    print('O valor da sua viagem será R$ {:.2f}'.format(d1))
else:
    d2 = k * 0.45
    print('O valor da sua viagem será R$ {:.2f}'.format(d2))

