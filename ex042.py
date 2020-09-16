a = int(input('digite o comprimeiro da primeira reta: '))
b = int(input('digite o comprimento da segunda reta: '))
c = int(input('digite o comprimento da terceira reta: '))
if ((b-c)<10<(b+c)) and ((a-c)<b<(a+c)) and ((a-b)<c<(a+b)):
    print('é possível criar um triângulo')
    if (a==b)and(a==c):
        print('o Triângulo é Equilatero')
    elif ((a==b) and (a!=c)) or ((a==c)and(a!=b)):
        print('o triangulo é Isóceles')
    elif ((a!=b)and(a!=c)and(b!=c)):
        print('O Triangulo é Escaleno')
else:
    print('não é possível criar um triangulo ')