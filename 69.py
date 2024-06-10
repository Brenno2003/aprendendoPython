cidade = 0
cm = 0
cfm20 = 0
print('-'*30)
print('      Cadastre de pessoa')
print('-'*30)
while True:
    nome = str(input('Qual o nome: '))
    while True:
        sexo = str(input('Qual o sexo(M/F): ')).strip().upper()
        sexo1 = sexo[0]
        if sexo1 == 'M' or sexo1 == 'F':
            break
    while True:
        idade = int(input('Qual a idade: '))
        if idade > 0:
            break
    if idade > 18:
        cidade += 1
    if sexo1 == 'M':
        cm += 1
    if idade < 20 and sexo1 == 'F':
        cfm20 += 1
    print('-' * 30)
    while True:
        add = str(input('Quer adicionar mais pessoas(S/N): ')).strip().upper()
        add1 = add[0]
        if add1 == 'S' or add1 == 'N':
            print('-' * 30)
            break
    if add1 == 'N':
        break
print(f'Tem {cidade} com mais de 18 anos\nTem {cm} homens\nTem {cfm20} mulheres com menos de 20 anos')
