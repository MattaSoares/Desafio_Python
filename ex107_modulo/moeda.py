# Modulo ex107

def metade(n):
    '''

    Metade de número
    :param n: Valor
    :return: Metade valor

    '''
    div = n / 2
    return div


def dobro(n):
    '''
    Cacula o valor do número
    :param n: valor
    :return: Dobro de valor
    '''
    mult = n * 2
    return mult


def aumentar(n, taxa):
    '''

    Função para aumentar um valor em determinada porcentagem.
    :param n: valor atual
    :param taxa: taxa a ser acrescentada
    :return: valor + taxa

    '''

    porcentagem = (n * taxa) / 100
    porcentagem_aumento = n + porcentagem
    return porcentagem_aumento


def diminuir(n, taxa):
    '''

    Função para diminuir um valor em determinada porcentagem
    :param n: valor atual
    :param taxa: taxa a ser diminuida
    :return: valor - porcentagem

    '''
    porcentagem = (n * taxa) / 100
    porcentagem_diminuir = n - porcentagem
    return porcentagem_diminuir

