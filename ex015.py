# um programa que calcule o preço a se pagar pelo aluguel de um carro.
km = float(input('quantos km foram rodados? '))
dia = float(input('quantos dias se passaram? '))
total = (dia*60)+(km*0.15)
print('o preço a se pagar é de R${}'.format(total))
