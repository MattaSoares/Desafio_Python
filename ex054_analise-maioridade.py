# Desafio 54 - Grupo da Maioridade
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final , mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# considere 18 anos como maioridade
from datetime import date
ano_atual = date.today().year
maioridade = 0
menoridade = 0
for i in range(1, 8):
    ano_nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoas são maiores de idade'.format(maioridade))
print('{} pessoas são menores de idade'.format(menoridade))
