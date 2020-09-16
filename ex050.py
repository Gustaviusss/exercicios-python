# um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, se
# o valor for ímpar, desconsidere-o.
soma = 0
for c in range(0, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
print('A Soma dos números pares é {}'.format(soma))