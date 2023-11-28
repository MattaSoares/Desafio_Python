# Desafio 115 - Projeto
'''Crie um pequeno sistema modularizado que permita cadastrar pessoas
pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções:
Cadastrar uma pessoa nova e listar todas as pessoas cadastradas.'''

from ex115_projeto.lib.Interface import *
from ex115_projeto.lib.arquivo import *
from time import sleep


def main():
    arquivo = 'cursoemvideo.txt'
    if not arquivoExiste(arquivo):
        criarArquivo(arquivo)
    while True:
        opcao = menu(['Lista de Usuários', 'Cadastrar Usuário', 'Sair'])
        if opcao == 1:
            lerArquivo(arquivo)
        elif opcao == 2:
            titulo('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = validaInt('Idade: ')
            cadastrar(arquivo, nome, idade)
        elif opcao == 3:
            titulo('Saindo..')
            break
        sleep(3)
    print('VOLTE SEMPRE!')


if __name__ == '__main__':
    main()

