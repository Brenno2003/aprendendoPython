n = int(input('esqueva um numero: '))
i = bin(n)
o = oct(n)
h = hex(n)
print('''[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
c = input('Qual opição voce quer: ').strip()
c2 = c.upper()
if c2 == '1':
    print('O valor em binário {}'.format(i[2:]))
elif c2 == '2':
    print('O valor em octal {}'.format(o[2:]))
elif c2 == '3':
    print('O valor em hexadecimal {}'.format(h[2:]))
else:
    print('Desculpa não temos essa opição')
