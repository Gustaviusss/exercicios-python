# um programa que checa o maior e menor número entre 3

n1 = int(input('digite um numero: '))
maior = n1
n2 = int(input('digite outro numero: '))
menor = n2
if n2>n1:
    maior = n2
    menor = n1
n3 = int(input('Digite outro numero: '))
if (n3>n2) and (n3>n1):
    maior = n3
else:
    menor = n3
print('o maior numero é {} e o menor é {}'.format(maior, menor))
