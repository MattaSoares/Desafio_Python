# Desafio 098 - Função de Contador
''' Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: Inicio, Fim e Passo e realize a contagem.
Seu Programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada. '''


def main():
    contador(1, 10, 1)
    contador(10, 0, 2)
    print('-=' * 30)
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    # Se o usuário digitar um número negativo, ele será transformado de volta para positivo
    # Se o usuário digitar zero, ele vira 1
    if passo < 0:
        passo = -1 * passo
    elif passo == 0:
        passo = 1
    contador(inicio, fim, passo)


def contador(inicio, fim, passo):
    from time import sleep
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM')
    else:
        for i in range(inicio, fim - passo, -passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM')


main()
