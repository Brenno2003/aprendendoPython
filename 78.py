lista = list(range(0, 5))
for c in range(0, 5):
    lista[c] = int(input(f'Numero na posição {c}: '))
print('=-'*50)
lista2 = lista[:]
lista2.sort()
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {lista2[4]} nas posições, ', end="")
for pos, c in enumerate(lista):
    if c == lista2[4]:
        print(f'{pos}...', end='')
print(f'\nO menor valor digitado foi {lista2[0]} nas posições, ', end='')
for pos, c in enumerate(lista):
    if c == lista2[0]:
        print(f'{pos}...', end='')
