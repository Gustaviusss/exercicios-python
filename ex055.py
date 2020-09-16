# um programa que leia o peso de 5 pessoas e mostre qual o maior e o menor peso.

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
        menor = maior
    elif peso < menor:
        menor = peso
print('o menor peso é {} e o maior é {}'.format(menor, maior))
