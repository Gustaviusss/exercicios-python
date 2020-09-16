# um programa que gere um número entre 1 e 5.

from random import randint
num = randint(1, 5)
chute = int(input('Que número entre 1 e 5 você acha que eu pensei? '))
if num == chute:
    print('Parabéns, você acertou!')
else:
    print('Eroooooou!!, eu pensei em {}'.format(num))
