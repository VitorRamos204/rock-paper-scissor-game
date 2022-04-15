from random import randint
from time import sleep

itens = ('Rock', 'Paper', 'Scissor')
computer = randint(0, 2)
print('''Suas opções:
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissor ''')
player = int(input('Choose rock, paper or scissor: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 12)
print('Player choose {}'.format(itens[player]))
print('Computer choose {}'.format(itens[computer]))
print('-=' * 12)
if computer == 0: # Computer choose Rock
    if player == 0:
        print('DRAW')
    elif player == 1:
        print('Player WIN!!')
    elif player == 2:
        print('Computer WIN!! ')
    else:
        print('INVALID MATCH')
elif computer == 1: # Computer choose Paper
    if player == 0:
        print('Computer WIN!!')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('Player WIN!!')
    else:
        print('INVALID MATCH')
elif computer == 2: # Computer choose Scissor
    if player == 0:
        print('Player WIN!!')
    elif player == 1:
        print('Computer WIN!!')
    elif player == 2:
        print('DRAW')
    else:
        print('INVALID MATCH')