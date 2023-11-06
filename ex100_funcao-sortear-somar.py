# Desafio 100 - Funções para sortear e somar
''' Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segynda função vai mostrar a soma entre todos os valores pares sorteados
pela função anterior .'''

def main():
    lista_sorteio = []
    sorteio(lista_sorteio)
    somaPar(lista_sorteio)

def sorteio(lista_sorteio):
    from random import randint
    from time import sleep
    print('Sorteando 5 valores da lista: ', end='')
    sleep(1)
    for i in range(0, 5):
        num = randint(0, 10)
        lista_sorteio.append(num)
        print(num, end=' ')
        sleep(0.5)
    print('Pronto!')


def somaPar(lista_sorteio):
    soma = 0
    for i in lista_sorteio:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista_sorteio}, temos {soma}')


main()
