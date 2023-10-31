# Desafio 087 - Matriz em Python 2
# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os números pares digitados
# b) A soma dos valores da terceira coluna
# c) O maior valor da segunda linha

matriz = []
dados = []
soma_par = valores_coluna3 = maior_valor_linha2 = 0
for i in range(0,3):
    for x in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{i}, {x}]: ')))
    matriz.append(dados[:])
    dados.clear()
print('-=' * 20)
for i in range(0,3):
    for x in range(0,3):
        print(f'[ {matriz[i][x]} ]', end=' ')
        if matriz[i][x] % 2 == 0:
            soma_par += matriz[i][x]
        if x == 2:
            valores_coluna3 += matriz[i][2]
        if i == 1:
            if matriz[1][x] > maior_valor_linha2:
                maior_valor_linha2 = matriz[1][x]
    print('')
print('-=' * 20)
print(f'A soma de todos os números pares: {soma_par}')
print(f'A soma dos valores da terceira coluna: {valores_coluna3}')
print(f'O maior valor da segunda linha: {maior_valor_linha2}')
