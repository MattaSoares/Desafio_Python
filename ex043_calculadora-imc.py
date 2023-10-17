# Desafio 043 - Calculadora IMC
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('\033[35m Calculadora de IMC')
print('¨¨\033[m' * 10)

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você tem o IMC de {:.1f}: Abaixo do peso'.format(imc))
elif imc <= 25:
    print('Você tem o IMC de {:.1f}: Peso ideal'.format(imc))
elif imc <= 30:
    print('Você tem o IMC de {:.1f}: Sobrepeso'.format(imc))
elif imc <= 40:
    print('Você tem o IMC de {:.1f}: Obesidade'.format(imc))
else:
    print('Você tem o IMC de {:.1f}: Obesidade Mórbida'.format(imc))
