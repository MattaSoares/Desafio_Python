# Desafio 083 - Listas: Analisando expressões matemáticas
# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
# ex: ((a+b)*c)(x+y(3+2/3)*z)

expressao_matematica = str(input('Digite um expressão matemática usando parênteses: ')).strip().lower()

aberto = 0
fechado = 0
for i in expressao_matematica:
    if i == '(':
        aberto += 1
    elif i == ')':
        fechado += 1
if aberto == fechado:
    print('\033[32mSua expressão está válida!')
else:
    print('\033[31mSua expressão está errada!')
