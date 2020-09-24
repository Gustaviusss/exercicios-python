# um programa que leia vários numeros inteiros e saia quando o usuario digitar 999
# como condição de saída, depois mostre quantos numeros foram digitados e a soma entre eles.


soma = num = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    num += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Foram contados {} números e a soma entre eles é de {}'.format(num-1, soma-999))
