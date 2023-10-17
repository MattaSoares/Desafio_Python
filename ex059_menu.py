# Desafio 059 - Menu de Opções
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior número
# [4] Novos números
# [5] Sair

from time import sleep
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
opcao = 0
while opcao != 5:
    print('''
    \033[1mMenu de Opções\033[m 
    [1] Somar
    [2] Multiplicar
    [3] Maior número
    [4] Novos números
    [5] Sair ''')
    opcao = int(input('>>>>Opção escolhida: '))

    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação entre {} x {} é {}'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print('O maior número digitado foi: {}'.format(maior))
        elif num2 > num1:
            maior = num1
            print('O maior número digitado foi: {}'.format(maior))
        else:
            print('Os valores são iguais')
    elif opcao == 4:
        print('Informe os números novamente')
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: '))
    elif opcao > 5:
        print('Valor incorreto. Tente novamente')
    print('=-' * 20)
    sleep(1)
print('Finalizando...')
sleep(1)
print('Fim do Programa')
