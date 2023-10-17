# Desafio 045 - Game: Jokempo
# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep
import pygame
pygame.init()
pygame.mixer.music.load('ex045.mp3')
pygame.mixer.music.play()

print('''
\033[1;33m JOKENPÔ 
...............................
\033[m
Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = str(input('Player: '))
jogada = int(input('Qual é a sua jogada? '))
maquina = randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')

print('')
print('\033[33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!\033[m')
print('')
if maquina == jogada:
    print('Maquina [\033[33m{}\033[m] X [\033[33m{}\033[m] {}\nEmpate'.format(itens[maquina], itens[jogada], jogador))
elif maquina == 0  and jogada == 1:
    print('Maquina [\033[31m{}\033[m] X [\033[32m{}\033[m] {}\nO jogador venceu!'.format(itens[maquina], itens[jogada], jogador))
elif maquina == 0 and jogada == 2:
    print('Maquina [\033[32m{}\033[m] X [\033[31m{}\033[m] {}\nA máquina venceu!'.format(itens[maquina], itens[jogada], jogador))
elif maquina == 1 and jogada == 0:
    print('Maquina [\033[32m{}\033[m] X [\033[31m{}\033[m] {}\nA máquina venceu!'.format(itens[maquina], itens[jogada], jogador))
elif maquina == 1 and jogada == 2:
    print('Maquina [\033[31m{}\033[m] X [\033[32m{}\033[m] {}\nO jogador venceu!'.format(itens[maquina], itens[jogada], jogador))
elif maquina == 2 and jogada == 0:
    print('Maquina [\033[31m{}\033[m] X [\033[32m{}\033[m] {}\nO jogador venceu!'.format(itens[maquina], itens[jogada], jogador))
elif maquina == 2 and jogada == 1:
    print('Maquina [\033[32m{}\033[m] X [\033[31m{}\033[m] {}\nA maquina venceu!'.format(itens[maquina], itens[jogada], jogador))
