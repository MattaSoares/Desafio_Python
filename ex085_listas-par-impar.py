# Desafio 085 - Listas com pares e impares
# Crie um programa onde o usário possa digitar sete valores numéricos
# e cadastreos em uma lista única que mantenha separadoros os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.

valores = [[], []]

for valor in range(1, 8):
    numero = int(input(f'Digite o {valor}° valor: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)

valores[0].sort()
valores[1].sort()
print('-=' *30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
