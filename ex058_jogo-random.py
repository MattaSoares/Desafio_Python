# Desafio 058 - Jogo: random 2.0
# Melhore o jogo do desafio 028 onde o computador vai pensar em um número de 0 a 10 .
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quanntos palpites foram necessarios para vencer.

import random
from time import sleep
print('\033[1;33m-=-' * 20)
print('\033[m  Eu pensei em um número de 0 a 10. Você consegue acertar?')
print('\033[1;33m-=-' * 20)
numero = random.randint(0,10)
acertou = False
contador = 0
while not acertou:
    tentativa = int(input('\033[mSeu palpite: '))
    print('Processando...')
    sleep(1)
    if tentativa == numero:
        acertou = True
    else:
        if tentativa > numero:
            print('Infelizmente você não acertou =(\n\033[34mTente um pouco menos...\033[m')
        else:
            print('Infelizmente você não acertou =(\n\033[33mTente um pouco mais...\033[m')
    contador += 1
print('\033[32m PARABÉNS!!!!! Você acertou depois de {} tentativas!'.format(contador))
