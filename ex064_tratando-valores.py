# Desafio 064 - Tratando vários valores
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usário deigitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
n = c = soma = 0
while n != 999:
    n = int(input('Digite o número:(\033[4m999 para sair\033[m)  '))
    if n != 999:
        soma += n
        c += 1
print('A soma dos {} valores digitados: {}'.format(c, soma))
