# Desafio 026 - Primeira e ultima ocorrencia de uma string
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra a
# - Em que posíção ela aparece a primeira vez
# - Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra "a" aparece na posição {}'.format(frase.find('a') + 1))
print('A última letra "a" aparece na posição {}'.format(frase.rfind('a') + 1))
