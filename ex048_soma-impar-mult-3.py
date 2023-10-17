# Desafio 048 - Soma ímpares multiplos de 3
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500
soma_impar_mult = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma_impar_mult += i
        contador += 1
print('A soma entre os {} números ímpares que são múltiplos de três no intervalo de 1 até 500 é:\n{}'.format(contador, soma_impar_mult))
