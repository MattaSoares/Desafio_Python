# Desafio 074 - Tupla: Maior e menor valores
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))
maior = tupla[0]
menor = tupla[0]
contador = 0
print('Os valores sorteados foram: ', end='')
for sorteio in tupla:
    print(sorteio, end=' ')
    if tupla[contador] > maior:
        maior = tupla[contador]
    elif tupla[contador] < menor:
        menor = tupla[contador]
    contador += 1

print(f'''
Maior: {maior}
Menor: {menor}
''')

# Utilizando métodos:
# print(f'O maior valor foi: {max(tupla)}')
# print(f'O menor valor foi: {min(tupla)}')
