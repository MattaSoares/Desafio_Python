# Desafio 49 - Tabuada 2.0
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('\033[33m=-' * 10)
print('      Tabuada')
print('=-' * 10)
num = int(input('\033[m  Tabuada do n° '))
for i in range(1, 11):
    print('{:5} x {:2} = {}'. format(num, i, i * num))
