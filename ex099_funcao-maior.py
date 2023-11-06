# Desafio 099 - Função que descobre o maior
''' Faça um programa que tenha uma funcao chamada maior()
que receba varios parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def main():
    maior(2, 9, 4, 5, 7, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()

def maior(* num):
    from time import sleep
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    maior = 0
    for i in num:
        print(i, end=' ')
        if i > maior:
            maior = i
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


main()
