casa = float(input('Digite o preço da casa: '))
sal = float(input('Digite o seu salário: '))
tempo = int(input('Em quantos anos deseja pagar? '))
parcela = casa / (tempo*12)
print('O Valor da parcela será de R${:.2f}'.format(parcela))
if parcela > (sal*0.30):
    print('Infelizmente seu empréstimo foi negado')
else:
    print('O Seu empréstimo foi aprovado')