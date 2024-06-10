from random import choice
from time import sleep
op = ['PEDRA', 'PAPEL', 'TESOURA']
j = input('Escolha a sua opição: ').strip()
j1 = j.upper()
x = choice(op)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('\033[37mx'*100)
print('\033[mComputador jogou {}'.format(x))
if x == j1:
    print('EMPATE')
elif x == 'PEDRA' and j1 == 'TESOURA':
    print('\033[31mPERDEU')
elif j1 == 'PEDRA' and x == 'TESOURA':
    print('\033[32mGANHOU')
elif j1 == 'TESOURA' and x == 'PAPEL':
    print('\033[32mGANHOU')
elif x == 'TESOURA' and x == 'PAPEL':
    print('\033[31mPERDEU')
elif j1 == 'PAPEL' and x == 'PEDRA':
    print('\033[32mGANHOU')
else:
    print('\033[31mPERDEU')
print('\033[37mx'*100)

