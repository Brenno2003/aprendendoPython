from random import shuffle
n = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
l = [n, n2, n3, n4]
shuffle(l)
print('{}'.format(l))




