# Desafio 004 - Dissecando uma variável
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

n = input('Digite algo: ')
print('O tipo primitivo de {} é {}'.format(n,type(n)))
print('{} só tem espaços? {}'.format(n, n.isspace()))
print('{} é numérico? {}'.format(n, n.isnumeric()))
print('{} é alfabético? {}'.format(n, n.isalpha()))
print('{} é alfanumérico? {}'.format(n, n.isalnum()))
print('{} está em maiúscula? {}'.format(n, n.isupper()))
print('{} está em minúscula? {}'.format(n, n.islower()))
print('{} está capitalizada? {}'.format(n, n.istitle()))
