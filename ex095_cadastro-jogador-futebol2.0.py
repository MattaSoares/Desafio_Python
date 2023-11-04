# Desafio 095 - Aprimorando os dicionários
# Aprimore o desafio 093 para que ele funcione com vários jogadores
# incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador

cadastro = dict()
gols = list()
time = list()

# Alimentando os dados de dicionario na lista
while True:
    cadastro.clear()
    print('-' * 30)
    cadastro['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    for i in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    time.append(cadastro.copy())
    gols.clear()
    while True:
        continua = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        if continua in 'sn':
            break
        print('Erro. Digite S para Sim ou N para não.')
    if continua == 'n':
        break


# Cabeçario da Tabela
print('-=' * 20)
print(f'{"Cod"}', end=' ')
for i in cadastro.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

# mostrando dados
for n, i in enumerate(time):
    print(f'{n:>3}', end='')
    for value in i.values():
        print(f' {str(value):<15}', end='')
    print()
print('-' * 40)

# Buscando informações personalizadas
while True:
    info = int(input('Info do Jogador: (Digite 999 para parar) '))
    if info == 999:
        break
    if info > len(time):
        print(f'Erro. Não existe jogador com o código {info}')
    else:
        print(f'--Levantamento do Jogador: {time[info]["nome"]}')
        for n, i in enumerate(time[info]['gols']):
            print(f'   No jogo {n + 1} fez {i} gols.')
        print('-' * 40)
print('<<< FIM >>>')
