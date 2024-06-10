while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    print("-"*30)
    if num >= 0:
        for c in range(0, 11):
            mut = num * c
            print(f'{num} x {c} = {mut}')
    else:
        break
    print("-" * 30)