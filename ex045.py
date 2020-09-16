from random import randint
p1 = input('pedra, papel ou tesoura?').lower().strip()
comandos = ['pedra', 'papel', 'tesoura']
pc = comandos[randint(0, 2)]
if (pc == 'pedra') and (p1 == 'tesoura'):
    print('{}, Ganhei!'.format(pc))
elif(pc == 'tesoura') and (p1 == 'papel'):
    print('{}, Ganhei!'.format(pc))
elif (pc == 'papel') and (p1 == 'pedra'):
    print('{}, Ganhei!'.format(pc))
elif (pc == 'pedra') and (p1 == 'papel'):
    print('{}, Você Ganhou!'.format(pc))
elif (pc == 'tesoura') and (p1 == 'pedra'):
    print('{}, Você Ganhou'.format(pc))
elif (pc == 'papel') and (p1 == 'tesoura'):
    print('{}, Você Ganhou!'.format(pc))
elif pc == p1:
    print('Empate!')