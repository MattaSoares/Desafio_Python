# Desafio 063 - Sequência de Fibonacci
# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma sequencia de fibonacci
# ex: 0 → 1 → 1 → 2 → 3 → 5 → 8 →
print('-' * 25)
print('\033[1m Sequência de Fibonacci\033[m')
print('-' * 25)
n = int(input('Quantos elementos você quer mostrar? '))
fibonacci_1 = 0
fibonacci_2 = 1
print('{} → '.format(fibonacci_1), end='')
print('{} → '.format(fibonacci_2), end='')

while n - 2 > 0:
    calculo_fibonacci = fibonacci_1 + fibonacci_2
    print('{} → '.format(calculo_fibonacci), end='')
    fibonacci_1 = fibonacci_2
    fibonacci_2 = calculo_fibonacci
    n -= 1
print('Fim', end='')
