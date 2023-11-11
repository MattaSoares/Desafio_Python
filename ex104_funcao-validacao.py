# Desafio 104 - Validando entrada de dados
''' Crie um programa que tenha a funçao leiaInt(), que vai funcionar de forma semelhante
á função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaint("Digite um número") '''


def main():
    n = leiaInt('Digite um número: ')
    print(f'Você acabou de digitar o número {n}')


def leiaInt(msg):
    ''' Função para validar se o que foi digitado é um número int válido.
    :param msg: mensagem do input
    :return: Se int retorna número '''
    while True:
        valida = str(input(msg))
        if valida.isnumeric():
            return int(valida)
            break
        else:
            print('\033[31mErro! Digite um número inteiro válido\033[m')


main()
