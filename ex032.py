ano = int(input('Digite um ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0) :
    print('o ano de {} é bissexto'.format(ano))
else:
    print('o ano de {} não é bissexto'.format(ano))
