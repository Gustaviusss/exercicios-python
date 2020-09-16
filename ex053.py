# um programa que leia uma frase qualquer e diga se é um palíndromo.
# apos a sopa, a sacada da casa, a torre da derrota, etc.

frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1] é outro jeito de fazer esse exercício usando fatiamento
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('{} ao contrário fica {}. É um palíndromo!!'.format(junto, inverso))
else:
    print('{} ao contrário fica {}. Não é um palíndromo!!'.format(junto, inverso))
