# Desafio 14 - Conversor de temperaturas
# Escreva um programa que converta um temperatura digitada em °C para °F

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = (celsius * 1.8) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(celsius, fahrenheit))
