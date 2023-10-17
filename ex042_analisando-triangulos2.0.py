# Desafio 042 - Analisando triângulos 2.0
# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: Todos os lados diferentes
print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite p valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print('Forma um triangulo equilátero')
    elif reta1 != reta2 != reta3 != reta1:
        print('Forma um triângulo escaleno')
    else:
        print('Forma um triângulo isósceles')
else:
    print('Não pode formar triângulo')
