# Desafio 036 - Emprestimo
# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o emprestimo será negado.


valor_imovel = float(input('Qual o valor do imóvel? R$'))
valor_salario = float(input('Quanto é o seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))
limite_prestacao = valor_salario * 30/100
valor_prestacao = valor_imovel / (anos * 12)

if valor_prestacao < limite_prestacao:
    print('\033[32m Seu empréstimo foi aprovado!\033[m \n O valor mensal será de {:.2f}'.format(valor_prestacao))
else:
    print('\033[31m Seu empréstimo foi negado.\033[m \n A prestação mensal de {:.2f} ultrapassou 30% do seu salário'.format(valor_prestacao))
