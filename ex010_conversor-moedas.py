# Desafio 10 - Conversor de Moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = 4.97
real = float(input('Quantos Reais você tem na carteira? R$'))
cotacao_dolar = 4.97
print('Com R${:.2f} você pode obter US${:.2f}'.format(real, real / cotacao_dolar))
