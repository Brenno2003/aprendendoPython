import random
v = random.randint(0, 5)
n = int(input('O computador escolheu um número de 0 a 5, tente adivinhar qual é: '))
if v == n:
    print('Você acertou!!!')
else:
    print('Você errou, tente novamente.')
    print('O número escolido pelo computador foi {}'.format(v))


