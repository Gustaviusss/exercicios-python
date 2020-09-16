# um programa que sorteie a ordem de apresentação de alunos
from random import shuffle
nome1 = input('primeiro aluno: ')
nome2 = input('segundo aluno: ')
nome3 = input('terceiro aluno: ')
nome4 = input('quarto aluno: ')
nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)
print('a ordem de apresentação será')
print(nomes)