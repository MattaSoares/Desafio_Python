# Desafio 082
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados.
# Ao final mostre o conteúdo das 3 listas geradas.

numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Gostaria de continuar? [S/N] ')).strip().lower()[0]
    if continua == 'n':
        break
#par & impar
par = list()
impar = list()
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'Números digitados: {numeros}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
