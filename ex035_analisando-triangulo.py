# Desafio 035 - Analisando Triângulo
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite p valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode formar um Triângulo')
else:
    print('Não pode formar triângulo')
