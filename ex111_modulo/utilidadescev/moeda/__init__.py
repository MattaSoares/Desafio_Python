# Modulo ex107

def metade(n, format=False):
    ''' Metade de número
    :param n: Valor
    :param format: Se o valor vai retornar formatado
    :return: Metade valor '''
    div = n / 2
    if format:
        return moeda(div)
    else:
        return div


def dobro(n, format=False):
    ''' Cacula o valor do número
    :param n: valor
    :param format: Retona formatado
    :return: Dobro de valor '''
    mult = n * 2
    if format:
        return moeda(mult)
    else:
        return mult


def aumentar(n, taxa, format=False):
    ''' Função para aumentar um valor em determinada porcentagem.
    :param n: valor atual
    :param taxa: taxa a ser acrescentada
    :pram format: Valor formatado
    :return: valor + taxa '''
    porcentagem = (n * taxa) / 100
    porcentagem_aumento = n + porcentagem
    if format:
        return moeda(porcentagem_aumento)
    else:
        return porcentagem_aumento


def diminuir(n, taxa, format=False):
    ''' Função para diminuir um valor em determinada porcentagem
    :param n: valor atual
    :param taxa: taxa a ser diminuida
    :param format: Valor formatado
    :return: valor - porcentagem '''
    porcentagem = (n * taxa) / 100
    porcentagem_diminuir = n - porcentagem
    if format:
        return moeda(porcentagem_diminuir)
    else:
        return porcentagem_diminuir


def moeda(n=0, moeda='R$'):
    ''' Valores com valor monetário formatado
    :param n: Valor
    :param moeda: Tipo da moeda
    :return: Valor formatado '''

    formatado = f'{moeda}{n:.2f}'.replace('.',',')
    return formatado


def resumo(preço=0, aumento=0, reducao=0):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preço, reducao, True)}')
    print('-' * 40)
