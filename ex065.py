#

soma = num = q = maior = menor = media = 0
op = 'S'
while op == 'S':
    num = int(input('Digite um número: '))
    op = str(input('deseja continuar?[S/N] ')).upper()
    soma += num
    q += 1
    if num > maior:
        maior = num
        menor = maior
    elif num < menor:
        menor = num
media = soma / q
print('Você digitou {} números e a media foi {:.2f}'.format(q, media))
print('o maior numero foi {} e o menor {}'.format(maior, menor))