# um programa que mostra a porção inteira de um numero float

from math import trunc
num = float(input('digite um numero: '))
print('a porção inteira de {} é {}'.format(num, trunc(num)))