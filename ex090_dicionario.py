# Desafio 090 - Dicionario em python
# Faça um programa que leia o nome e média de um aluno guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

alunos = dict()

alunos['Nome'] = str(input('Nome do Aluno: '))
alunos['Media'] = float(input(f'Média de {alunos["Nome"]}: '))

if alunos['Media'] >= 7:
    alunos['Situacao'] = 'Aprovado'
elif 5 <= alunos['Media'] < 7:
    alunos['Situacao'] = 'Recuperação'
else:
    alunos['Situacao'] = 'Reprovado'

print('-' * 20)

for key, value in alunos.items():
    print(f'- {key} é igual a {value}')
