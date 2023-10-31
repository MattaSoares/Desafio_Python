# Desafio 086 - Matriz em python
# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.
# no final mostre a matriz na tela com a formatação correta.

matriz = []
dados = []
for i in range(0,3):
    for x in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{i}, {x}]: ')))
    matriz.append(dados[:])
    dados.clear()

for i in range(0,3):
    for x in range(0,3):
        print(f'[ {matriz[i][x]:^5} ]', end=' ')
    print()
