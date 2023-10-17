# Desafio 056 - Analise de Pessoa
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos

soma_idade = 0
homem_velho = 0
nome_velho = ''
total_fem_20 = 0
for i in range(1,5):
    print('=-= {}° Cadastro =-='.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()
    print('-=' * 10)
    soma_idade += idade
    if sexo == 'm':
        if idade > homem_velho:
            nome_velho = nome
    elif sexo == 'f':
        if idade < 20:
            total_fem_20 += 1
media = soma_idade / 4
print('Media de idade do grupo: {:.2f} anos'.format(media))
print('O nome do homem mais velho: {}'.format(nome_velho))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(total_fem_20))
