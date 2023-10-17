# Desafio 34 - Aumento múltiplos
# Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? R$ '))
if salario > 1250.00:
    novo_salario = salario + (salario * 10/100)
    print('O novo salário com o aumento de 10% será: {:.2f}'.format(novo_salario))
else:
    novo_salario = salario + (salario * 15/100)
    print('O novo salário com o aumento de 15% será: {:.2f}'.format(novo_salario))
