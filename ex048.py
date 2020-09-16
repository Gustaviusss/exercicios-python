# Um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
# e que se encontram no intervalo de 1 até 500
soma = 0
for c in range(0, 500):
    if (c % 3 == 0) and (c % 2 != 0):
        soma += c
print('a soma dos números ímpares múltiplos de 3 entre 1 e 500 é {}'.format(soma))