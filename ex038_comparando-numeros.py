# Desafio 38 - Comparando números
# Escreva um programa que leia dois números inteiros e compare-os, mostrando:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Os dois valores são iguais

valor1 = int(input('Digite o Primeiro valor: '))
valor2 = int(input('Digite o Segundo valor: '))
if valor1 > valor2:
    print('O PRIMEIRO valor é o maior!')
elif valor2 > valor1:
    print('O SEGUNDO valor é o maior!')
else:
    print('Os valores são IGUAIS!')
