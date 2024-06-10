op = 'S'
soma = 0
c = 0
while op == 'S':
    num = int(input('Digite um numero: '))
    op1 = str(input('Quer continuar(S/N): ')).strip().upper()
    op = op1[0]
    soma += num
    c += 1
    med = soma/c
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('O maior é {}, o menor é {}, a media é {}'.format(maior, menor, med))

