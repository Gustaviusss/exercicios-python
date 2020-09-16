n = int(input('Digite um numero: '))
mult = 0

for count in range(2, n):
    if n % count == 0:
        print('é múltiplo de {}'.format(count))
        mult += 1
if mult == 0:
    print('É Primo!')
else:
    print('Tem {} múltiplos acima de 2 e abaixo de {}'.format(mult, n))