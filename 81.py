lista = list()
while True:
    lista.append(int(input('Adicione um numero: ')))
    op = input('Quer continuar(S/N): ').strip().upper()[0]
    if op == 'N':
        break
    elif op not in 'SN':
        while True:
            op = input('Valor invalido tende novamente, Quer continuar(S/N): ').strip().upper()[0]
            if op[0] in 'NS':
                break
print('-='*50)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
