from random import randint
numeros_aleatorios = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os numeros forteados foram {numeros_aleatorios[0]}, {numeros_aleatorios[1]}, {numeros_aleatorios[2]}, '
      f'{numeros_aleatorios[3]}, {numeros_aleatorios[4]}')
maior = sorted(numeros_aleatorios)[4]
menor = sorted(numeros_aleatorios)[0]
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
