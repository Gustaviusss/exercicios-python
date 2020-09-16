# um programa que calcula aumento de salário

sal = float(input('Digite seu salário: '))
if sal > 1250:
    sal = sal + (sal*0.10)
else:
    sal = sal + (sal*0.15)
print('Seu salario com aumento é de R${:.2f}'.format(sal))
