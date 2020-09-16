# um programa que mostre seno, coseno e tangente de um angulo
from math import sin, cos, tan, radians
ang = float(input('digite um angulo: '))

sen = sin(radians(ang))
csen = cos(radians(ang))
tg = tan(radians(ang))

print('O angulo {} tem os valores {:.2f}, {:.2f} e {:.2f} como seno, cosseno e tangente, respectivamente.'.format(ang, sen, csen, tg))