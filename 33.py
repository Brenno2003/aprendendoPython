n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
n3 = int(input('Escolha um terceiro número: '))
if n1 >= n2 and n1 >= n3:
    print('O {} é o maior número'.format(n1))
if n2 >= n1 and n2 >= n3:
    print('O maior número é {}'.format(n2))
if n3 >= n1 and n3 >= n2:
    print('{} é o maior número'.format(n3))
if n1 <= n2 and n1 <= n3:
    print('O {} é o menor número'.format(n1))
if n2 <= n1 and n2 <= n3:
    print('O menor número é {}'.format(n2))
if n3 <= n1 and n3 <= n2:
    print('{} é o menor número'.format(n3))


