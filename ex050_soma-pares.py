# Desafio 050 - Soma dos pares
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma_par = 0
contador = 0
for i in range(1,7):
    num = int(input('Digite o {}° número: '.format(i)))
    if num % 2 == 0:
        soma_par += num
        contador += 1
print('A soma dos {} números pares digitados foi: {}'.format(contador, soma_par))
