listagem = ('Lapis', 1.75, 'Borracha', 2, 'Cderno', 15.90, 'Estijo', 25, 'Mochila', 120.32)
print('-'*50)
print(f'{'Listagem de preço':^50}')
print('-'*50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*50)

