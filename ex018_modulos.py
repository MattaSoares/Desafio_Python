# Desafio 18 - Utilizando módulos
# Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo {}° possui o Seno {:.2f}, Cosseno {:.2f} e a Tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
