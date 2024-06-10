lista = list()
listapar = list()
listaimpa = list()
while True:
    num = (int(input('Adicione um numero: ')))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpa.append(num)
    op = input('Quer continuar(S/N): ').strip().upper()[0]
    if op == 'N':
        break
    elif op not in 'SN':
        while True:
            op = input('Valor invalido tende novamente, Quer continuar(S/N): ').strip().upper()[0]
            if op[0] in 'NS':
                break
print('-='*50)
print(f'A lista completa {lista}')
print(f'A lista de pares é {listapar}')
print(f'A listar de impares é {listaimpa}')
