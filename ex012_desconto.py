# Desafio 12 -  Calculando Desconto
# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 5 / 100
novo_preco = preco - desconto
print('Produto com 5% de desconto: R${:.2f}'.format(novo_preco))
