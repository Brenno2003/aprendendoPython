numeros = (int(input('Digite uma numero: ')), int(input('Digite uma numero: ')), int(input('Digite uma numero: ')), int(input('Digite uma numero: ')))
print(f'O numero 9 apareceu {numeros.count(9)}')
if 3 in numeros:
    print(f'O nuemro 3 apareceu na posição {numeros.index(3)}')
c = 0
for d in range(0, 4):
    if numeros[d] % 2 == 0:
        c += 1
print(f'Foram digitados {c} numeros pares')
