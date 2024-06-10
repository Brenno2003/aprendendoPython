a = int(input('Qual ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('É ano bissextos')
else:
    print('Não é ano bissextos')