# um programa que tire a média entre duas notas e exiba uma mensagem de acordo.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5.0:
    print('Você está reprovado. Nota: {}'.format(media))
elif 6.9 > media > 5.0:
    print('Você está de recuperação. Nota: {}'.format(media))
else:
    print('Você está aprovado. Nota: {}'.format(media))
