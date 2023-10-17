# Desafio 011 - Pintando Parede
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m*2.

largura_parede = float(input('Digite a largura da parede: '))
altura_parede = float(input('Digite a altura da parede: '))
area = largura_parede * altura_parede
qtd_tinta = area / 2

print(' Área: {}m² \n Quanlidade de tinta necessária: {}l'.format(area, qtd_tinta))
