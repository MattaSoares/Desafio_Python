# Desafio 077 - Tuplas: Contando vogais
# Crie um programa que tenha uma tupla com várias palavras
# Depois disso você deve mostrar, para cada palavra, quais são as suas vogais

lista = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for palavra in lista:
    print(f'\nNa palavra \033[32m{palavra}\033[m temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
