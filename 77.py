listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'CURSO')
for c in listagem:
    print(f'\nNa palavra {c} temos',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f',{letra}', end='')