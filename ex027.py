# um programa que mostra o primeiro e último nome

nome = input('Digite seu nome completo: ')
nome = nome.split()
print('Primeiro nome:', nome[0])
print('Último nome: ', nome[len(nome)-1])
