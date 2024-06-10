from random import randint
c = 0
print("=-"*30)
print("Vamos jogar par ou ímpar")
print("=-"*30)
while True:
    num2 = randint(0, 10)
    num = int(input("Escolha um numero: "))
    soma = num + num2
    op = str(input("Quer Par ou Ímpar (P/I): ")).strip().upper()
    print("-" * 30)
    print(f'Você jogou {num} e o computador jogou {num2} o resultado é {soma}')
    print("-" * 30)
    if op == 'P':
        if soma % 2 == 0:
            c += 1
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("=-" * 30)
        else:
            print('Você Predeu')
            print("=-" * 30)
            break
    else:
        if soma % 2 != 0:
            c += 1
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("=-" * 30)
        else:
            print('Você Predeu')
            print("=-" * 30)
            break
print(f'Game Over! Você venceu {c}')


