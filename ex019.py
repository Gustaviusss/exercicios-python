# um programa que sorteie um aluno
from random import randint
nome1 = input('primeiro aluno: ')
nome2 = input('segundo aluno: ')
nome3 = input('terceiro aluno: ')
nome4 = input('quarto aluno: ')
nomes = [nome1, nome2, nome3, nome4]
print('o sorteado foi {}!'.format(nomes[randint(0,3)]))
