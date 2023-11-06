# Desafio 097 - Um print especial
''' Faça um programa que tenha uma função chamada escreva()
que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adptavel '''

def main():
    escreva("Mateus Soares")
    escreva("Curso de Python no YouTube")
    escreva("CeV")


def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


main()
