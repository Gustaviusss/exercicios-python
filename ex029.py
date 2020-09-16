vel = int(input('Qual a velocidade do carro? '))
vel_max = 80
if vel > vel_max:
    multa = 7 * (vel - vel_max)
    print('Você está acima da velocidade e deverá pagar multa de R${:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade permitida.')
print('==FIM==')