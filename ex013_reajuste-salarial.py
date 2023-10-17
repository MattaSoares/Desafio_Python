# Desafio 013 - Reajuste Salarial
# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario * 15/100
novo_salario = salario + aumento
print('O novo salário com 15% de aumento: R${:.2f}'.format(novo_salario))
