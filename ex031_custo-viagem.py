# Desafio 031 - Custo da viagem
# Desenvolva um programa que pergunte s distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km
# e R$0,45 para viagens mais longas.

viagem = int(input('Quantos km você gostaria de viajar? '))
#Simplificado: preco_passagem = viagem * 0.50 if viagem <= 200 else viagem * 0.45
if viagem <= 200:
    preco_passagem = viagem * 0.50
else:
    preco_passagem = viagem * 0.45
print('Preço da Passagem: R${}'.format(preco_passagem))
