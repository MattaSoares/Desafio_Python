# Desafio 19 - Sorteando um item na lista
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
aluno1 = input('Escreva o nome do 1° aluno: ')
aluno2 = input('Escreva o nome do 2° aluno: ')
aluno3 = input('Escreva o nome do 3° aluno: ')
aluno4 = input('Escreva o nome do 4° aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print('O aluno sorteado foi: {}'.format(sorteio))
