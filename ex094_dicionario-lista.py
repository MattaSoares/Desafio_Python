# Desafio 094 - Unindo dicionários e listas
# Crie um programa que leia nome, sexo e idade de várias pessoas
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idade acima da media

#leitura de dados
pessoas = dict()
lista_pessoas = list()
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().lower()[0]
        if pessoas['sexo'] in 'mf':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    lista_pessoas.append(pessoas.copy())
    pessoas.clear()
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continua in 'sn':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if continua == 'n':
        break

for i in lista_pessoas:
    for key, value in i.items():
        if key == 'idade':
            soma += value
# analise de dados
media = soma / len(lista_pessoas)
print('=-' * 30)
print(f'- Foram cadastradas {len(lista_pessoas)} pessoas.')
print(f'- A média de idade do grupo é: {media:.1f}')
print(f'- As mulheres cadastradas foram: ', end='')
for p in lista_pessoas:
    if p['sexo'] in 'f':
        print(f'{p["nome"]} ', end=' ')
print()
print(f'- Pessoas com idade acima da média:')
for i in lista_pessoas:
    if i['idade'] > media:
        print(' ', end='')
        for key, value in i.items():
            print(f'{key} = {value}; ', end=' ')
        print()
print('<< Encerrado >>')
