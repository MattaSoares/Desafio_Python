# Desafio 068 - Jogo: Par ou ímpar
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from time import sleep
from random import randint
print('-=' * 20)
print('     Vamos jogar Par ou Ímpar!')
print('-=' * 20)
vitoria = 0
while True:
    maquina = randint(0, 10)
    decisao = ' '
    while decisao not in 'pi':
        decisao = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    n = int(input('Qual o seu número? '))
    total = maquina + n
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    print(f'Você jogou {n} e o computador jogou {maquina}. Total: {total}')
    if decisao == 'p' and total % 2 == 0:
        vitoria += 1
        print('\033[32mDeu par. Você ganhou!\033[m')
        print('-=' * 20)
        print('Vamos jogar novamente', end='')
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
    elif decisao == 'i' and total % 2 == 1:
        vitoria += 1
        print('\033[32mDeu ímpar. Você ganhou!\033[m')
        print('-=' * 20)
        print('Vamos jogar novamente', end='')
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
    else:
        print(f'\033[31mVocê perdeu depois de {vitoria} vitórias seguidas!\033[m')
        print('-=' * 20)
        break
print('Fim do Programa')
