# Desafio 061 - Progressão Aritmética 2.0
# Refaça o desafio 052 lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('=== Gerador de PA ===')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 10
while contador > 0:
    print('{}→ '.format(primeiro_termo), end='')
    primeiro_termo += razao
    contador -= 1
print('Fim', end='')
