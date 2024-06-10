n1 = float(input('Qual a sua primeira nota: '))
n2 = float(input('Qual a sua segunda nota: '))
m = (n1+n2)/2
print('A media do aluno foi {:.2f}'.format(m))
if m < 5:
    print('\033[31mREPROVADO')
elif 5 <= m < 7:
    print('\033[33mRECUPERAÇÃO')
else:
    print('\033[32mAPROVADO')
