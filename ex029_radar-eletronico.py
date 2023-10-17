# Desafio 29 - Radar Eletronico
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

vel_carro = int(input('Qual é a velocidade do carro em km/h: '))
if vel_carro > 80:
    multa = (vel_carro - 80) * 7
    print('\033[31m Você foi multado em R${:.2f} por exceder o limite permitido de 80km/h nessa via.'.format(multa))
else:
    print('\33[32m Parabéns! Continue sendo um excelente cidadão.')
