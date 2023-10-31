# Desafio 088 - Mega Sena
# Faça um programa que ajude a criar palpites.
# O programa vai perguntar quantos jogos serão gerafos e vai sortear 6 números entre 1 e 60 para cada jogo
# cadastrando tudo em uma lista composta.

from time import sleep
from random import randint
print('-' * 40)
print(f'{"Mega Sena":^40}')
print('-' * 40)
qtd_palpites = int(input('Quantas sequencias você gostaria de fazer? '))
print(f'-=-=-=-= Sorteando {qtd_palpites} sequencias =-=-=-=-')
palpites = list()
contador = 0
for i in range(1, qtd_palpites + 1):
    while True:
        n = randint(1, 60)
        if n not in palpites:
            palpites.append(n)
            contador += 1
            if contador == 6:
                contador = 0
                break
    palpites.sort()
    print(f'Sorteio {i}: {palpites}')
    palpites.clear()
    sleep(1)
print('-=' * 20)
