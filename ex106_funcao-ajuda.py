# Desafio 106 - Sistema interativo de Ajuda
''' Faça um mini sistema que utilize o interective helpdo python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra fim, o progrma se encerrará. '''


def main():
    from time import sleep
    while True:
        menu('Sistema de ajuda PyHelp', 2)
        inicio = str(input('Função ou Biblioteca --> '))
        if inicio.lower() == 'fim':
            break
        menu(f'Acessando o manual do {inicio}', 3)
        sleep(1)
        help(inicio)
        sleep(1)
    menu('Até logo!', cor=1)


def menu(msg, cor=0):
    c = ['\033[m',# 0: Sem Cor
         '\033[0;30;41m',# 1: Vermelho
         '\033[0;30;43m',# 2: Amarelo
         '\033[0;30;44m'# 3: Azul
         ]
    print(c[cor], end='')
    print('-' * len(msg))
    print(f'{msg}')
    print('-' * len(msg))
    print(c[0], end='')


main()
