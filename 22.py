nome = input('Qual o seu nome: ').strip()
M = nome.upper()
m = nome.lower()
s = nome.split()
cl = len(''.join(s))
cp = len(s[0])
print('''Analisando nome 
Seu nome em letra maiuscula é {}
Seu nome em lenta minuscula é {}
Seu nome tem {} letras
Seu primeiro nome é {} e ele tem {} letras'''.format(M, m, cl, s[0], cp))




