n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro número é maior'.format(n1))
elif n2 > n1:
    print('O segundo número é maior'.format(n2))
else:
    print('Ele são iguais')
