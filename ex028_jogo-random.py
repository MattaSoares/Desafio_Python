# Desafio 028 - Jogo random
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
print('\033[1;33m-=-' * 20)
print('\033[m  Eu pensei em um número de 0 a 5. Você consegue acertar?')
print('\033[1;33m-=-' * 20)
numero = random.randint(0,5)
tentativa = int(input('\033[m Numero: '))
print('Processando...')
sleep(2)
if numero == tentativa:
    print('\033[32m PARABÉNS!!!!! Você acertou!')
else:
    print('\033[31mSinto muito. Eu pensei no número {} não no {}. Tente novamente.'.format(numero, tentativa))
