n = int(input("Digite ate que numero: "))
a = 0
b = 1
c = 0
while n > 0:
    print(' {}'.format(a), end='')
    a = b + c
    b = c
    c = a
    n -= 1





