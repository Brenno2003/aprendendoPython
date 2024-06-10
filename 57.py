sexo = 'Q'
while sexo != '':
    sexo = input("Qual o seu sexo (M/F): ").strip().upper()
    s = sexo[0]
    if s == 'M' or sexo == 'F':
        sexo = ''

    else:
        print("\033[31mResposta invalida tente novamente\033[m")
        print("")
