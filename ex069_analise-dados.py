# Desafio 69 - Analise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

print('-' * 20)
print('{:^20}'.format('CADASTRO DE PESSOAS'))
print('-' * 20)
mais_18 = homens = mulher_menos_20 = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        mais_18 += 1
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    if sexo == 'm':
        homens += 1
    elif sexo == 'f':
        if idade < 20:
            mulher_menos_20 += 1
    print('-' * 20)
    continua = ' '
    while continua not in 'sn':
        continua = str(input(('Quer continuar? [S/N] '))).strip().lower()[0]
    if continua == 'n':
        break
    print('-' * 20)
print('=== Fim do Programa ===')
print(f'Total de pessoas com mais de 18 anos: {mais_18}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher_menos_20} mulheres com menos de 20.')
