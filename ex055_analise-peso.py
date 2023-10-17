# Desafio 055 - Maior e menor valor
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.

maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(i)))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print('O menor peso digitado foi: {}kg'.format(menor_peso))
print('O maior peso digitado foi: {}kg'.format(maior_peso))
