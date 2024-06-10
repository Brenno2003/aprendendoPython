tabela = ('PALMEIRAS', 'GREMIO', 'ATLETICO-MG', 'FLAMENGO', 'BOTAFOGO', 'BRAGANTINO', 'FLUMINENSE', 'ATHLETICO-PR',
          'INTERNACIONAL', 'FORTALEZA', 'SAO PAULO', 'CUIABA', 'CORINTHIAS', 'CRUZEIRO', 'VASCO', 'BAHIA',
          'SANTOS', 'GOIAS', 'CORITIBA', 'AMERICA-MG')
while True:
    print('''Escolha a opção:
                A) Os 5 primeiros
                B) OS 4 Últmos
                C) Umas lista dos times em ordem alfabética
                D) Escolher um time para vé a posição''')
    while True:
        op = input('Escolha uma opção: ').strip().upper()
        if op in 'ABCD':
            if op == 'A':
                print(tabela[0:6])
            elif op == 'B':
                print(tabela[16:])
            elif op == 'C':
                print(sorted(tabela))
            elif op == 'D':
                nome_time = input('Digite o nome do seu time: ').strip().upper()
                time = tabela.index(nome_time)+1
                print(f'O time {nome_time} esta na {time} posição')
            break
        else:
            print('Tente novamente', end='')
    op_continuar = input('Quer continuar (S/N)').strip().upper()[0]
    if op_continuar == 'N':
        break
