# Desafio 066 - Varios números com flag
# Crie um programa que leia varios números inteiros pelo teclado.
# o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
n = soma = c = 0
while True:
    n = int(input('Digite um valor: (999 para parar) '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'A soma dos {c} valores foi {soma}')
