c = 0
i = 0

while c == 0:
    ini = str(input("Quer fazer uma operação matematica(S/N):")).strip().upper()
    ini1 = ini[0]
    if ini1 == 'N':
        print("Ok")
    else:
        i = 1
    while i == 1:
        opcao = 0
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digitr outro número: "))
        while opcao != 6:
            print("=" * 100)
            print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novo número
[5] Sair''')
            opcao = int(input("Digite aqui a opcao: "))
            if opcao == 1:
                resultado = n1 + n2
                print("A soma de {} com {} é {}".format(n1, n2, resultado))
            elif opcao == 2:
                resultado = n1 * n2
                print("A multiplicão de {} com {} é {}".format(n1, n2, resultado))
            elif opcao == 3:
                maior = n1
                if n2 > n1:
                    maior = n2
                print("O maior número é {}".format(maior))
            elif opcao == 4:
                opcao = 6
            else:
                opcao = 6
                i = 0

