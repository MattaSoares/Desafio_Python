# Desafio 070 - Estatisticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de 1000.
# c) Qual é o nome do produto mais barato.
print('-' * 20)
print('{:^20}'.format('LOJAS SUPER BARATÃO'))
print('-' * 20)
total_compra = qtd_mil = menor_preco = 0
produto_barato = ''
while True:
    produto_nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total_compra += preco
    if preco > 1000:
        qtd_mil += 1
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        produto_barato = produto_nome
    continua = ' '
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continua == 'n':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {qtd_mil} produtos custando mais de R$1000.00')
print((f'O produto mais barato foi {produto_barato} que custa R${menor_preco:.2f}'))
