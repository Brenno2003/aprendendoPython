nome = str(input('Seu nome: ')).strip()
n1 = nome.split()
print('''É um prazer de conhecer
Seu primeiro nome é {}
Seu ultimo nome é {}'''.format(n1[0], n1[len(n1)-1]))

