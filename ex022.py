# um programa que calcula a quantidade de caracteres em um nome
nome = input("Digite seu nome completo: ")
nome_queb = nome.split()
nome_sem = ''.join(nome_queb)
print(nome.upper())
print(nome.lower())
print('seu nome tem', len(nome_sem), 'caracteres')
print('quantidade de letras no primeiro nome:', len(nome.split()[0]))
