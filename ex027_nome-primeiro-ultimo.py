# Desafio 027 - Primeiro e ultimo nome
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o últiimo nome
# separadamente

nome = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[-1]))
