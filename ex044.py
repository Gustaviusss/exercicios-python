preco = float(input('Digite o preço normal do produto: '))
pag = int(input(
    """Escolha entre uma das formas de pagamento abaixo:
    1: Dinheiro/cheque(10% de Desconto).
    2: À Vista no cartão(5% de desconto).
    3: 2x no cartão.(preco normal)
    4: 3x ou mais no cartão(20% de juros)"""))
if pag == 1 :
    preco = preco - (preco * 0.1)
    print('o preço do produto será de R${:.2f}'.format(preco))
elif pag == 2:
    preco = preco - (preco * 0.05)
    print('o preço do produto será de R${}'.format(preco))
elif pag == 3:
    print('o produto manterá o preço normal de R${}'.format(preco))
else:
    preco = preco + (preco * 0.2)
    print('O preco do produto será de R${}'.format(preco))