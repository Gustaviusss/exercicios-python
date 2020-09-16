# Um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética) e
# mostre na tela os 10 primeiros números dessa progressão

print('==Gerador de Progressão Aritmética==')
p1 = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a razão: '))
n = p1
for c in range(0, 10):
    print(n)
    n = n + r
print('==Fim==')