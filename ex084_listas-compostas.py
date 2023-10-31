# Desafio 084 - Lista composta e analise de dados
# Faça um programa que leia o nome e peso de várias pessoas, quardando tudo em uma lista.
# No final, mostre:
# a) quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves

pessoas = list()
dados = list()
mais_pesado = list()
menos_pesado = list()
qtd = total = media = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    qtd += 1
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continua == 'n':
        break

for p in pessoas:
    total += p[1]

media = total / qtd

for i in pessoas:
    if i[1] > media:
        mais_pesado.append(i[0])
    elif i[1] <= media:
        menos_pesado.append(i[0])

print(f'Foram cadastradas {qtd} pessoas')
print(f'Os mais pesados, que estão acima da média de {media:.1f} kg, são: {mais_pesado}')
print(f'Os mais leves, que estão abaixo da média de {media:.1f} kg, são: {menos_pesado}')
