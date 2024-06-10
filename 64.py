a = 0
c = 0
soma = 0
num = int(input('Digite um numero: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('Digite um numero: '))
print("A soma foi de {} e foram digitados {} numeros".format(soma, c))
