# Desafio 051 - Progressão Aritmética
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
print(primeiro_termo, end='→ ')
pa = primeiro_termo
for i in range(0, 9):
    pa += razao
    print(pa, end='→ ')
print('Fim')
