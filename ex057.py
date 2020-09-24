# um programa que leia o sexo de uma pessoa mas só aceite M ou F como entrada

sexo = str(input('Digite seu sexo [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    print('Inválido, tente novamente.')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()

if sexo == 'M':
    print('Masculino')
elif sexo == 'F':
    print('Feminino')
