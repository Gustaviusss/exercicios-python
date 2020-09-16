import datetime
now = datetime.datetime.now()
ano = now.year
quant = 0
for c in range(0, 7):
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    if ano - ano_nasc >= 21:
        quant += 1
print('{} pessoas dessa lista já são maiores de idade.'.format(quant))
