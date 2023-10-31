# Desafio 089: Boletim com listas compostas
# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cado aluno individualmente.
alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continua == 'n':
        break
print('-=' * 20)
print(f'{"N°":<3}{"NOME":<20}{"MÉDIA":>9}')
print('-'* 40)
for i in range (0, len(alunos)):
    print(f'{i:<3}{alunos[i][0]:<20}{alunos[i][2]:>8.1f}')
print(f'-=' * 20)
while True:
    registro = int(input('Mostrar as notas de qual aluno? [Digite 999 para sair] '))
    if registro == 999:
        break
    print(f'As notas de {alunos[registro][0]} são: {alunos[registro][1]}')
print('Fim')
