# Desafio: 005 - Antecessor e Sucessor
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
print(' Número digitado: {} \n Antecessor: {} \n Sucessor: {} \n'.format(num, (num - 1), (num + 1)))
