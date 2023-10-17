# Desafio 053 - Detector de palíndromo
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# ex: Palíndromo, segundo o dicionário Houaiss, “diz-se de ou frase ou palavra que se pode ler, indiferentemente,
# da esquerda para direita ou vice-versa”:
# osso, Ana, radar, Renner, Roma é amor, socorram me subi no onibus em Marrocos
# a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona

# Minha solução
frase = str(input('Digite uma frase: ')).lower().strip().split()
frase_normal = ''.join(frase)
frase_reverso = ''

for i in range(len(frase_normal) - 1, -1, -1):
    frase_reverso += frase_normal[i]

if frase_normal == frase_reverso:
    print('A frase é um Palíndromo.\nNormal: {}\nReverso: {}'.format(frase_normal, frase_reverso))
else:
    print('A frase não é um Palíndromo.\nNormal: {}\nReverso: {}'.format(frase_normal, frase_reverso))


#Solução Professor: não é necessário o for em python
#frase = str(input('Digite uma frase: ')).lower().strip().split()
#frase_normal = ''.join(frase)
#frase_reverso = frase_normal[::-1]

#if frase_normal == frase_reverso:
#    print('A frase é um Palíndromo.\nNormal: {}\nReverso: {}'.format(frase_normal, frase_reverso))
#else:
#    print('A frase não é um Palíndromo.\nNormal: {}\nReverso: {}'.format(frase_normal, frase_reverso))
