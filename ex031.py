distancia = int(input('Digite a distancia da sua viagem em KM: '))
if distancia <= 200:
    preco = distancia * 0.50
    print('O Preço da sua viagem é R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('o preco da sua viagem é de R${:.2f}'.format(preco))
