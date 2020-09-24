# Refazer o exercício 051 usando while

p1 = int(input('Digite o Número: '))
r = int(input('Razão da PA: '))
n = p1
c = 0
while c < 10:
    print('{}'.format(n), end='')
    print(' -> ' if c < 10 else '', end='')
    c += 1
    n += r
print('Fim da PA')