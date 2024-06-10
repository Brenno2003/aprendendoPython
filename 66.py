num = 0
c = 0
soma = 0
while True:
    num = int(input('digite um numero (Digite 999 para parar) : '))
    if num == 999:
        break
    soma += num
    c += 1
print(f"Foram digitados {c} números, e a soma de todos eles é {soma}")
