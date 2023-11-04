# Desafio 093 - Cadastro de jogador de futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
cadastro = dict()
gols = list()
cadastro['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'    Quantas partidas {cadastro["nome"]} jogou? '))
for i in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
cadastro['gols'] = gols[:]
cadastro['total'] = sum(gols)
print('-=' * 30)
print(cadastro)
print('-=' * 30)
for key, value in cadastro.items():
    print(f'O campo {key} tem o valor {value}.')
print('-=' * 30)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')
for i, x in enumerate(gols):
    print(f'     => Na partida {i + 1}, fez {x} gols.')
print(f'Fez o total de {cadastro["total"]} gols.')
