soma = 0
for c in range(0, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
print('A Soma dos números pares é {}'.format(soma))