# um programa que leia dois valores e mostre um menu na tela
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
while op != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]novos números
    [5]Sair''')
    op = int(input('qual é a sua opção? '))
    if op == 1:
        print('a soma entre {} e {} é {}'.format(n1, n2, (n1+n2)))
    elif op == 2:
        print('{} x {} é igual a {}'.format(n1, n2, (n1*n2)))
    elif op == 3:
        if n1 > n2:
            print('{} é maior'.format(n1))
        elif n2 > n1:
            print('{} é maior'.format(n2))
        else:
            print('os dois são iguais')
    elif op == 4:
        print('informe os numeros novamente.')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif op == 5:
        print('finalizando...')
    else:
        print('opção inválida, tente novamente.')
    print('=-=' * 10)
print('fim do programa')
