# Desafio 075 - Tuplas: Analise de Dados
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.
numeros = (int(input(f'Digite um valor: ')), int(input(f'Digite outro valor: ')), int(input(f'Digite mais um valor: ')), int(input(f'Digite o último valor: ')))
print(f'Você digitou os valores: {numeros}')

# a
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

# b
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print('O valor 3 não foi encontrado')

# c
print(f'Os valores pares digitados foram: ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')
