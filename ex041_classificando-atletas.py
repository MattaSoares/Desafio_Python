# Desafio 041 - Classificando atletas
# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: Mirim
# até 14 anos: Infantil
# até 19 anos: Junior
# até 25 anos: Sênior
# acima: Master
from datetime import date
data_hoje = date.today().year

print('\033[34m-=\033[m'* 17)
print('\033[1mConfederação Nacional de Natação\033[m')
print('\033[34m-=\033[m'* 17)
print('Bem vindo!')

data_nasc = int(input('Em qual ano você nasceu? '))
idade = data_hoje - data_nasc

if idade <= 9:
    print('Com {} anos você está na categoria: Mirim'.format(idade))
elif idade <= 14:
    print('Com {} anos você está na categoria: Infantil'.format(idade))
elif idade <= 19:
    print('Com {} anos você está na categoria: Junior'.format(idade))
elif idade <= 25:
    print('Com {} anos você está na categoria: Senior'.format(idade))
else:
    print('Com {} anos você está na categoria: Master'.format(idade))
