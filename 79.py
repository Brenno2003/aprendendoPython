num = []
while True:
    a = (int(input('Digite um valor: ')))
    if a in num:
        print('Valor duplicado, não foi adicionado...')
    else:
        num.append(a)
        print('Valor adicionado com sucesso...')
    op = input('Quer continuar(S/N): ').strip().upper()[0]
    if op[0] not in 'NS':
        while True:
            op = input('Valor invalido tende novamente, Quer continuar(S/N): ').strip().upper()[0]
            if op in 'NS':
                break
    if op[0] == 'N':
        break
print('=-'*50)
num.sort()
print(f'Os valores digitados foi {num}')

