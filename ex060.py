# um programa que calcula fatorial

# <--Usando Módulos-->
# from math import factorial
# n = int(input('Digite um número: '))
# f = factorial(n)
# print('O Fatorial de {} é {}'.format(n, f))
# <--Usando Módulos-->

# <--Usando While-->
# n = int(input('Digite um número: '))
# c = n
# f = 1 # usa-se 1 quando se precisa de uma multiplicação limpa, pois qualquer numero * 1 é o proprio numero.
# while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f *= c
#    c -= 1
# print('{}'.format(f))
# <--Usando While-->

# Usando For

n = int(input('Digite um número: '))
c = n
f = 1
for c in range(c, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))

