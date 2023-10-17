# Desafio 060 - Calculo do fatorial
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120

print('\033[1;34mFatorial\033[m')
fatorial = int(input('Digite um valor: '))
calculo_fatorial = 1
print('Calculando {}! = '.format(fatorial), end='')
while fatorial > 0:
    print('{}'.format(fatorial), end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    calculo_fatorial *= fatorial
    fatorial -= 1
print('{}'.format(calculo_fatorial))

# Usando bibliotecas:
# from math import factorial
# n = int(input('Digite um número para calcular o seu fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))
