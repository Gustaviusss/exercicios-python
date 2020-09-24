# melhorar o ex028 usando while

from random import randint

num = randint(0, 11)
c = 1
chute = (int(input('Em que numero de 0 a 10 eu pensei? ')))
while chute != num:
    chute = int(input('Errou!, tente novamente. '))
    c += 1
if c > 1:
    print('Parabéns! Você acertou com {} tentativas.'.format(c))
else:
    print('Parabéns! Você acertou com {} tentativa.'.format(c))