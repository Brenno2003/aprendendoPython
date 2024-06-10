a = 1
b = 1
ex = str(input('Digite uma expressão: '))
for c in ex:
    if c == '(':
        b += 1
    if c == ')':
        a += 1
if b != a:
    print('Expreção invalida')
elif ex[0] == ')':
    print('Expressão invalida')
elif ex[-1] == '(':
    print('Expressão invalida')
else:
    print('Expressão valida')



