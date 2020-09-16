# Um programa que leia um número inteiro e diga se ele é primo ou não
n = int(input('Digite um numero: '))
mult = 0

for count in range(2, n): # o contador se inicia em 2 pois antes do 2 só tem 1
    if n % count == 0: # se o módulo da divisão por algum número diferente de 1 for 0 o número não é primo
        print('é múltiplo de {}'.format(count))
        mult += 1 # recebe a quantidade de múltiplos que o número tem
if mult == 0:
    print('É Primo!')
else:
    print('Tem {} múltiplos acima de 2 e abaixo de {}'.format(mult, n))