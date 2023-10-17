# Desafio 030 - Par ou Impar
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é Par'.format(num))
else:
    print('O número {} é Ímpar'.format(num))
