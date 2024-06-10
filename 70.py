print('-'*30)
print(f'{'Loja Super barato':^30}')
print('-'*30)
c = 0
soma = 0
mqm = 0
menor = 0
menorp = 0
while True:
    nome = str(input('Qual o nome do produto: ')).strip()
    p = float(input('Qual o preço: R$ '))
    c += 1
    soma += p
    if p > 1000:
        mqm += 1
    if c == 1:
        menor = nome
        menorp = p
    else:
        if p < menorp:
            menorp = p
            menor = nome
    while True:
        op = str(input('Quer comtinuar (S/N): ')).strip().upper()
        op1 = op[0]
        if op1 == 'S' or op1 == 'N':
            break
    if op1 == 'N':
        break
print(f'{'Fim do programa':-^40}')
print(f'O total foi de R${soma:.2f}\nTEMOS {mqm} que custam mais que R$1000\nO produto mais barato foi a {menor} custando R${menorp:.2f}')



