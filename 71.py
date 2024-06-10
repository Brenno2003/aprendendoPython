print('='*30)
print(f'{'Banco':^30}')
print('='*30)
ced = 50
saced = 0
sac = int(input('Qual o valaor que você vai sacar: '))
while True:
    if sac >= ced:
        sac -= ced
        saced += 1
    else:
        if saced > 0:
            print(f'Total de {saced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        saced = 0
        if sac == 0:
            break