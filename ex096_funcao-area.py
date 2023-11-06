# Desafio 096 - Função que calcula área
''' Faça um programa que tenha uma função chamada área()
que receba as dimensões de um terreno retangular(largura e comprimento)
e mostre a area do terreno '''

def main():
    print(f'{"Controle de terrenos":^30}')
    print('-' * 30)
    l = float(input("Largura (m): "))
    c = float(input('Comprimento (m): '))
    area(l, c)

def area(l, c):
    area_terreno = l * c
    print(f'A area do terreno de {l} x {c} é {area_terreno}m²')


main()
