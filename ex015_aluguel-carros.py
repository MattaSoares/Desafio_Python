# Desafio 15 - Aluguel de Carros
# Escreva um programa que pergunte a quantidade de dias
# e a quantidade de km percorridos por um carro alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
total_pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total_pagar))
