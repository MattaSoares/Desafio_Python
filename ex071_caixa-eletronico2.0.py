# Desafio 071 - Simulador de Caixa Eletrônico
# Crie um progrma que simule o funcionamento de um caixa eletrônico.
# No inicio pergunte ao usuário qual será o valor a ser sacado. (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$200, R$100, R$50, R$20, R$10, R$5, R$2, R$1

from ex071_modulo import *

def main():
    valor = menu()
    qtd_notas = operacao(valor)
    saida_notas(qtd_notas)


if __name__ == '__main__':
    main()

