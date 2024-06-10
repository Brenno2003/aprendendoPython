import random
n = input('peimeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
l = [n, n2, n3]
r = random.choices(l)
print('O aluno escolido foi {}'.format(r))