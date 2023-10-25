# Desafio 078 - Listas: Maior e menor
# Faça um programa que leia 5 valores numériocos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
posicoes_maior = list()
posicoes_menor = list()

for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {i+1}: ')))
# Resolvendo da maneira raiz:
#    if i == 0:
#        maior = numeros[0]
#        menor = numeros[0]
#    elif numeros[i] > maior:
#        maior = numeros[i]
#    elif numeros[i] < menor:
#        menor = numeros[i]
maior = max(numeros)
menor = min(numeros)
for p in range(0, len(numeros)):
    if numeros[p] == maior:
        posicoes_maior.append(p+1)
    elif numeros[p] == menor:
        posicoes_menor.append(p+1)
print('=-' * 20)
print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i in posicoes_maior:
    print(i, end='...')
print('')
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for i in posicoes_menor:
    print(i, end='...')
