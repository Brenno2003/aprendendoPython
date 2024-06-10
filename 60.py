num = int(input('Digite um número em fatorial: '))
c = num
mut = 1

while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    mut *= c
    c -= 1

print('{}'.format(mut))




