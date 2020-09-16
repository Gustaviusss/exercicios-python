# um programa que procura letras numa frase

frase = input('digite uma frase: ').lower().strip()

print('quantidade de letras A', frase.count('a'))
print('a primeira letra foi encontrada na posição {}'.format(frase.find('a')+1))
print('a ultima letra foi encontrada na posição {}'.format(frase.rfind('a')+1))

