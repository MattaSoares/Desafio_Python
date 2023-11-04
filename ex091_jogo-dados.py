# Desafio 091 - Jogo de dados
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {
    'jogador_1': randint(1, 6),
    'jogador_2': randint(1, 6),
    'jogador_3': randint(1, 6),
    'jogador_4': randint(1, 6)}
ranking = list()

print('Resultados:')
for key, value in jogadas.items():
    sleep(1)
    print(f'{key} tirou {value} no dado.')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print()

print('== Ranking ==')
for i, v in enumerate(ranking):
    print(f'Em {i + 1}° lugar está o {v[0]} com {v[1]} no dado')
