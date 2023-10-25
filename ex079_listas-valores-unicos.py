# Desafio 079 - Listas: Valores únicos
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list()
while True:
    novo_valor = int(input('Digite um valor: '))
    continua = ' '
    if novo_valor in valores:
        print('Não é possível adicionar valores duplicados')
    else:
        valores.append(novo_valor)
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N] ')).strip().lower()
    if continua == 'n':
        break
valores.sort()
print('=-' * 20)
print(f'Você digitou os valores {valores}')
print('Fim')
