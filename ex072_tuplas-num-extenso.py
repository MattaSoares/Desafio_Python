# Desafio 072 - Tuplas: Número por extenso
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até Vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('\033[31mErro. Tente novamente. \033[m', end='')
    print(f'\033[32mO número {n} por extenso é: {extenso[n]}\033[m')
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continua == 'n':
        break
print('Fim')
