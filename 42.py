l1 = float(input('Qual o primeiro lado: '))
l2 = float(input('Qual o segundo lado: '))
l3 = float(input('Qual o segundo lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('É possivel criar um triangulo', end=',')
    if l1 == l2 == l3:
        print(' e o triangulo será equilatero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print(' e o triangulo será isósceles')
    else:
        print(' e o triangulo será escaleno')
else:
    print('Não tem como formar um triangulo')
