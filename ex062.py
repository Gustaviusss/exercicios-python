# melhorar o ex061

p1 = int(input('Digite o Número: '))
r = int(input('Razão da PA: '))
n = p1
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print('{} -> '.format(n), end='')
        c += 1
        n += r
    print('pausa')
    mais = int(input('quantos numeros quer mostrar a mais?'))
print('Progressão finalizada com {} termos'.format(total))
