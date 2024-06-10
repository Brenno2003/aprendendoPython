nome_num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'catoze',
            'Quinze', 'Dezeseis', 'Dezesete','Dezoito',
            'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while True:
        if 0 <= num <= 20:
            break
        else:
            num = int(input('Tente novamente. Digite um número: '))

    print(f'O número digitado foi {nome_num[num]}')
    op = input('Quer continuar (S/N): ').strip().upper()[0]
    if op == 'N':
        break
