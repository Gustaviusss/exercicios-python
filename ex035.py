a = int(input('digite o comprimeiro da primeira reta: '))
b = int(input('digite o comprimento da segunda reta: '))
c = int(input('digite o comprimento da terceira reta: '))
if ((b-c)<10<(b+c)) and ((a-c)<b<(a+c)) and ((a-b)<c<(a+b)):
    print('é possível criar um triângulo')
else:
    print('não é possível criar um triangulo ')