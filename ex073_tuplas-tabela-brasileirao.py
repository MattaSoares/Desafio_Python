# Desafio 073 - Tuplas: Tabela do Brasileirão
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
# Depois mostre:
# a) Os 4 primeiros colocados.
# b) Os últimos 4 colocados
# c) Em que posição está o Vasco.
# d) Times na ordem alfabética.
brasileirao_2023 = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Athletico-PR', 'Flamengo', 'Fortaleza',
                    'Fluminense', 'Atlético-MG', 'Cuiabá', 'São Paulo', 'Internacional', 'Bahia', 'Cruzeiro',
                    'Corinthians', 'Vasco', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

# 4 primeiros
print('\033[1mBrasileirão 2023\033[m')
for i in range(0,4):
    print(i + 1,brasileirao_2023[i])
print('.........')

# 4 ultimos
for i in range(16,20):
    print(i + 1, brasileirao_2023[i])

# Que posição está o vasco
print('=-' * 20)
print(' ')
print('O vasco está na posição {}° da tebela'.format(brasileirao_2023.index('Vasco') + 1))
print(' ')

# Ordem alfabética
print('=-' * 20)
ordem = sorted(brasileirao_2023)
print('\033[1mTabela Em Ordem Alfabética\033[m')
for times in ordem:
    print(times)
