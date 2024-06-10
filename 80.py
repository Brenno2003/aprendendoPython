lista = list()
for c in range(0, 5):
    num = int(input('Digite uma valor: '))
    if c == 0 or num >= lista[len(lista)-1]:
        lista.append(num)
        print('O valor foi adicionado no final da lista')
    else:
        for pos, el in enumerate(lista):
            if num < el:
                lista.insert(pos, num)
                print(f'O numero foi adicionado na posição {pos}')
                break
print('=-'*50)
print(f'Os valores digitados em ordem foram {lista}')
