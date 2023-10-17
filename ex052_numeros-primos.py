# Desafio 052 - Números primos
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
contador_primo = 0
for i in range(1, num + 1):
    if num % i == 0:
        contador_primo += 1
        print('\033[34m{} '.format(i), end='')
    else:
        print('\033[m{} '.format(i), end='')

if contador_primo == 2:
    print('\nO número {}, divisível apenas por 1 e por ele mesmo, é primo.'.format(num))
else:
    print('\nO número {}, divisivel por {} números, NÃO é primo.'.format(num, contador_primo))
