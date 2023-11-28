# Desafio 113 - Tratamento de erros - Funções aprofundadas
'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
de digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.'''


def main():
    n_int = leiaInt('Digite um número inteiro: ')
    n_float = leiaFloat('Digite um número Real: ')
    print(f'Você acabou de digitar o número inteiro {n_int} e o Real {n_float}')


def leiaInt(msg):
    ''' Função para validar se o que foi digitado é um número int válido.
    :param msg: mensagem do input
    :return: Se int retorna número '''
    while True:
        try:
            num = int(input(msg))
            return num
        except (ValueError, TypeError):
            print(f'\033[31mErro: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\nO usuário interrompeu a entrada de dados')
            break


def leiaFloat(msg):
    ''' Função para validar se o que foi digitado é um número float válido.
    :param msg: mensagem do input
    :return: Se float retorna número '''
    while True:
        try:
            num = float(input(msg))
            return num
        except (ValueError, TypeError):
            print(f'\033[31mErro: por favor, digite um número Real válido.\033[m')
        except KeyboardInterrupt:
            print('\nO usuário interrompeu a entrada de dados')
            break


main()
