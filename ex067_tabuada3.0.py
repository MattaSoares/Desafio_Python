# Desafio 067 - Tabuada 3.0
# Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    print('-' * 20)
    for i in range(1, 10):
        print(f'{tabuada:5} x {i:2} = {tabuada * i}')
        i += 1
    print('-' * 20)
print('Programa Encerrado')
