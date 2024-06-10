p = float(input('Qual o valor: '))
fp = input('Qual a forma de pagamento é cartão, á vista ou cheque: ').strip()
fp1 = fp.upper()
if fp1 == 'Á VISTA' or fp1 == 'A VISTA' or fp1 == 'CHEQUE':
    pv = p - p * 0.1
    print('O valor com o desconto será de R${}'.format(pv))
elif fp1 == 'CARTÃO' or fp1 == 'CARTAO':
    cd = input('Credito ou Debito: ').strip()
    cd2 = cd.upper()
    if cd2 == 'DEBITO':
        pv = p - p * 0.05
        print('O valor com desconto é de R${}'.format(pv))
    elif cd2 == 'CREDITO':
        pa = int(input('Será em quantas vezes: '))
        if pa <= 2:
            pv = p / pa
            print('A parcela será de R${}, o valor total será de R${}'.format(pv, p))
        elif pa > 2:
            pv = p + p * 0.2
            npv = pv/pa
            print('O valor da parcela será de R${}, e o valor total será de R${}'.format(npv, pv))


