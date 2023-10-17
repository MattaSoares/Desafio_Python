# Desafio 024 - Verificando as primeiras letras de um texto
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".

cidade = str(input('Escreva o mome da sua cidade: ')).strip().lower().split()
verifica = cidade[0] == 'santo'
print(verifica)
