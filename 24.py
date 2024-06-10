C = str(input('Em qual cidade você nasceu: ')).strip()
C2 = C.upper()
C3 = C2.split()
s = 'SANTO' in C3[0]
print('É True ou False que a cidade que você nasceu começa com Santo: {}'.format(s))




