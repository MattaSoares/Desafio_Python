# Desafio 103 - Ficha do jogador
''' Faça um programa que tenha uma função chamada ficha(), que receba dois parametros
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, msm que algum dado não tenha
sido informado corretamente '''

def main():
    nome = str(input('Nome do Jogador: '))
    gols = str(input('Numero de Gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        print(ficha(g=gols))
    else:
        print(ficha(nome, gols))
def ficha(n='<desconhecido>', g='0'):
    return f'O jogador {n} fez {g} gol(s) no campeonato.'

main()
