# um programa que checa se o nome da cidade começa com "Santo" ou  não

city = str(input('Digite o nome da cidade: ')).strip().upper()
if city[:5] == 'SANTO':
    print('A Cidade começa com Santo')
else:
    print('a cidade não começa com santo')