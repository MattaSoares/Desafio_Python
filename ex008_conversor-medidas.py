# Desafio 008 - Conversor de Medidas
# Escreva um program que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_metros = float(input('Digite um valor em metros: '))
print(' {}m corresponde a {:.0f}cm e {:.0f}mm.'.format(valor_metros, (valor_metros * 100), (valor_metros * 1000)))
