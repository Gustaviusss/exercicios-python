# um programa que diga quantos litros de tinta são necessários para pintar uma parede

width = float(input('qual a largura da parede? '))
height = float(input('qual a altura da parede? '))
area = width*height
lt = 2
tinta = area/lt
print('sua parede tem {:.2f}m² e você precisa \nde {:.2f} de litros de tinta para pintar essa parede'.format(area, tinta))
