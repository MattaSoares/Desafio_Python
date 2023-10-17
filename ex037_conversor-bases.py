# Desafio 37 - Conversor de Bases
# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''
Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31m Opção Inválida')
