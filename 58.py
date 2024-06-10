from random import randint
n1 = randint(0, 10)
print("O computador pensou em um numero tente acertar")
n2 = -1
c = 0
while n1 != n2:
    n2 = int(input("Tente acertar o numero: "))
    c += 1

print("Precisou de {} tentativas para acerta".format(c))





