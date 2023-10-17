# Desafio 039 - Alistamento militar
# Faça um programa que leia o ano de nascimento de um jovem, e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora dele se alistar
# - Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('\033[32mAlistamento Militar\033[m')
genero = str(input('Você é Homem? [S/N] ')).strip()
if genero.lower() == 's':
    ano_nasc = int(input('Qual o ano do seu nascimento? '))
    data_hoje = date.today().year
    idade = data_hoje - ano_nasc
    if idade == 18:
        print('Você já completou {} anos. Aliste-se na junta militar mais próxima!'.format(idade))
    elif idade < 18:
        saldo = 18 - idade
        print('Você tem {} anos. Ainda faltam {} anos para você se alistar. Seu alistamento será em {}'.format(idade, saldo, data_hoje + saldo))
    else:
        saldo = idade - 18
        print('Você tem {} anos. Você já deveria ter se alistado a {} anos. Seu alistamento foi em {}'.format(idade, saldo, data_hoje - saldo))
else:
    print('As mulheres não precisam fazer o alistamento obrigatório.')
