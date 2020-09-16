# a tabuada de um número escolhido pelo usuário

num = int(input('digite um numero: '))
for x in range(1, 11):
    print('{}*{}={}'.format(num, x, (num*x)))
