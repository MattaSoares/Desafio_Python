# Desafio 101 - Funções para votação
''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. '''

def main():
    ano_nsc = int(input('Em que ano você nasceu? '))
    print(voto(ano_nsc))

def voto(nascimento):
    ''' Função para determinar se uma pessoa deve votar este ano
    :param nascimento: um parametro para ano
    :return: string '''
    from datetime import date
    hoje = date.today().year
    idade = hoje - nascimento
    if 18 <= idade < 65:
        return f'Com {idade} anos é OBRIGATÓRIO votar!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos é OPCIONAL votar!'
    else:
        return f'Com {idade} anos é NEGADO votar!'


main()
