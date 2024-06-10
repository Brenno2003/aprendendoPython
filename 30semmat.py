par = ['2', '4', '6', '8', '0']
n = str(input('Escolha um número: ')).strip()
un = n[len(n)-1]
if un in par:
    print('O número é par')
else:
    print('O número é ímpar')


