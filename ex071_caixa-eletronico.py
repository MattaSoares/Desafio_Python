# Desafio 071 - Simulador de Caixa Eletrônico
# Crie um progrma que simule o funcionamento de um caixa eletrônico.
# No inicio pergunte ao usuário qual será o valor a ser sacado. (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$200, R$100, R$50, R$20, R$10, R$5, R$2, R$1
print('=' * 20)
print('  CAIXA ELETRÔNICO')
print('=' * 20)
duzentos = cem = cinquenta = vinte = dez = cinco = dois = um = 0
valor = int(input('Digite o valor a ser sacado: R$ '))
while True:
    if valor >= 200:
        duzentos += 1
        valor -= 200
    elif valor >= 100:
        cem += 1
        valor -= 100
    elif valor >= 50:
        cinquenta += 1
        valor -= 50
    elif valor >= 20:
        vinte += 1
        valor -= 20
    elif valor >= 10:
        dez += 1
        valor -= 10
    elif valor >= 5:
        cinco += 1
        valor -= 5
    elif valor >= 2:
        dois +=1
        valor -= 2
    elif valor >= 1:
        um += 1
        valor -= 1
    else:
        break
print(f'''
\033[1mValor        | Qtd de Notas\033[m
Duzentos:    |   {duzentos} 
Cem:         |   {cem}
Cinquenta:   |   {cinquenta} 
Vinte:       |   {vinte}
Dez:         |   {dez}  
Cinco:       |   {cinco}
Dois:        |   {dois}  
Um:          |   {um}
''')
print('Volte sempre!')
