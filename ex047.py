# Um programa que mostre todos os numeros pares entre 1 e 50

for c in range(1, 50):
    if c % 2 == 0: # se c % 2 != 0 o programa mostraria todos os ímpares
        print(c)
        print('-')
print('==Fim==')