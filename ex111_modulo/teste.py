# Desafio 111 - Transformando módulos em pacotes
''' Crie um pacote utilidadesCeV que tenha dois modulos internos
chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109
para o primeiro pacote e mantenha tudo funcionando. '''

from ex111_modulo.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 10, 5)
