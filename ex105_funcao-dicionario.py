# Desafio 105: Analisando e Gerando Dicionários
''' Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''


def main():
    resp = notas(10, 9.5, 8.5, sit=True)
    print(resp)


def notas(*num, sit=False):
    '''

    ---> Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas de alunos
    :param sit: (valor opcional) indica se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.

    '''
    dict_notas = dict()
    dict_notas['total'] = len(num)
    dict_notas['maior'] = max(num)
    dict_notas['menor'] = min(num)
    dict_notas['média'] = sum(num) / len(num)
    if sit:
        if dict_notas['média'] > 8:
            dict_notas['situação'] = 'Ótima'
        elif dict_notas['média'] > 7:
            dict_notas['situação'] = 'Boa'
        elif dict_notas['média'] > 6:
            dict_notas['situação'] = 'Regular'
        else:
            dict_notas['situação'] = 'Ruim'
    return dict_notas


main()
