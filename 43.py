P = float(input('Qual é o seu peso: (Kg) '))
A = float(input('Qual a sua altura: (m) '))
IMC = P / A**2
print('O IMC dessa pessoa é {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
elif 40 <= IMC:
    print('Obesidade mórbida')
