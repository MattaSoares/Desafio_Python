# Desafio 102 - Função para fatorial
''' Crie um programa que tenha uma função fatorial()
 que receba dois parâmetros: o primeiro que indique o número a calcular
 e o outro chamado show, que será um valor lógico (opcional)
 indicando se será mostrado ou não na tela o processo de calculo do fatorial. '''

def main():
    print(fatorial(5, True))


def fatorial(n, show=False):
    '''
    --> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) True para mostrar a conta.
    :return: O valor do fatorial (f) '''
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


main()
#help(fatorial)
