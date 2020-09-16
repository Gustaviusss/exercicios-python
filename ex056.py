somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
menores = 0

for p in range(1, 5):
    print("-----{}ª Pessoa-----")
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        menores += 1
print('A média de idade das pessoas é de {}'.format(somaidade/4))
print('o homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('existem {} mulheres menores de 20 anos no grupo:'.format(menores))