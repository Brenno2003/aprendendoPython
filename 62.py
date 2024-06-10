c = 0
f = 10
num = int(input('Qual o primeiro termo: '))
ra = int(input('Qual a razão: '))
nom = ''
nom1 = ''
while nom1 != 'N':

    while c != f:
        print('{}'.format(num), end=', ')
        num = num + ra
        c += 1
    nom = str(input("\n Quer ver mais termos(S/N): ")).strip().upper()
    nom1 = nom[0]
    if nom1 == 'S':
        mt = int(input("Quer ver mais quantos termos: "))
        f += mt
print('Fim do programa')
