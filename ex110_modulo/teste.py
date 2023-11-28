# Desafio 110 - Reduzindo seu programa
''' Adicione ao modulo moedas.py uma função chamada resumo(),
que mostre na tela algumas informações geredas pelas funções que já temos
no modulo criado até aqui '''

from ex107_modulo import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 10, 5)
