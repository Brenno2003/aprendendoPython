frase = str(input('Digete uma frase: ')).strip()
k = frase.lower()
k2 = k.count('a')
c = k.find('a')
b = k.rfind('a')
print('''A letra A aparece vezes {}
A letra A aparece pela primeira vez na posição {}
A letra A apareceu pela ultima vez na posição {}'''.format(k2, c + 1, b + 1))




