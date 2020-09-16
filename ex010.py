br = float(input('quantos reais você tem? '))
dollar = br / 3.27
if dollar==1:
    print('você pode comprar {} dólar'.format(dollar))
else:
    print('você pode comprar {:.2f} dólares'.format(dollar))
