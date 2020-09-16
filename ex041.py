import datetime
now = datetime.datetime.now()
ano_atual = now.year
ano = int(input('digite o ano de nascimento: '))
idade = ano_atual - ano
if idade <= 9:
    print('Mirin')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Júnior')
elif idade == 20:
    print('Sênior')
else:
    print('Master')