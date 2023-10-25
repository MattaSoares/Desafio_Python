# Desafio 081: Listas: Extraindo dados
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# a) Quantos números foram digitados.
# b) A lista de valores , ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista

numeros = list()
contador = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    contador += 1
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Gostaria de continuar? [S/N]' )).strip().lower()[0]
    if continua == 'n':
        break
print(f'Foram digitados {contador} números')
numeros.sort(reverse=True)
print(f'Lista decrescente: {numeros}')
if 5 not in numeros:
    print('O número 5 não está na lista')
else:
    print('O valor 5 está na lista')
print('Fim')
