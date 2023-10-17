# Desafio 032 - Ano Bissexto
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date
ano = int(input('Quais anos são Bissextos? Digite um ano ou aperte 0 para saber o atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
