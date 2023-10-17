# Desafio 065 - Maior e menor valores
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a media entre todos os valores
# e qual foi o maior e menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continua = True
contador = soma = maior = menor = 0
while continua == True:
    n = int(input('Digite um valor: '))
    contador += 1
    soma += n
    if maior and menor == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    sequencia = str(input('Gostaria de continuar? [S \ N] ')).strip().lower()[0]
    if sequencia == 'n':
        continua = False
media = soma / contador
print('Você digitou {} números e a média foi {}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
