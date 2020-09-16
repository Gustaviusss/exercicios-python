# um programa para aprovar um empréstimo bancário para compra de uma casa
# ler o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# calcular o valor da prestação mensal sabendo que ela não pode exceder 30% do
# salário do comprador ou o empréstimo será negado.

casa = float(input('Digite o preço da casa: '))
sal = float(input('Digite o seu salário: '))
tempo = int(input('Em quantos anos deseja pagar? '))
parcela = casa / (tempo*12)
print('O Valor da parcela será de R${:.2f}'.format(parcela))
if parcela > (sal*0.30):
    print('Infelizmente seu empréstimo foi negado')
else:
    print('O Seu empréstimo foi aprovado')