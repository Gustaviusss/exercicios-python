sal = float(input('qual o seu salário? '))
novo_sal = sal + (sal*0.15)
print('o seu salario é de R${}, com aumento é de R${:.2f}'.format(sal, novo_sal))