# Desafio 025 - Procurando um string dentro de outra
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('Qual é o seu nome completo? ')).strip().lower()
print('silva' in nome)
