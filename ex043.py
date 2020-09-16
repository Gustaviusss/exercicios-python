# um programa que calcule o imc e mostre o resultado na tela

alt = float(input('digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt*alt)
print('Seu Imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc < 25:
    print('Peso Ideal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')