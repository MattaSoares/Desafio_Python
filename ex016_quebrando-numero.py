# Desafio 16 - Quebrando um número
# Crie um programa que leia um número Real qualquer e mostre na tela a sua porção Inteira.

import random
from math import trunc

num = random.uniform(1, 100)
porcao_inteira = trunc(num)
print('Número digitado: {}'.format(num))
print('O número {} tem a parte inteira {}'.format(num, porcao_inteira))
