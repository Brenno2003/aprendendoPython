l1 = int(input('Linha 1: '))
l2 = int(input('Linha 2: '))
l3 = int(input('Linha 3: '))
if l1 + l2 > l3 and l3 + l2 > l1 and l1 + l3 >l2:
    print('É possivel fazer um triângulo')
else:
    print('Não é possivel fazer um triângulo')
