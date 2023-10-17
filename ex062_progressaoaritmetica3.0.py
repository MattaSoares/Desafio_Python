# Desafio 62 - Super progressao aritmetica
# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa se encerra quando ele disser que quer mostrar 0 termos.

print('=== Gerador de PA ===')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
continua = True
contador = 10
qtd_termo = 10
while continua == True:
    while contador > 0:
        print('{}→ '.format(primeiro_termo), end='')
        primeiro_termo += razao
        contador -= 1
    print('Fim')
    pergunta_continua = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    print('-=' * 10)
    if pergunta_continua == 'S':
        contador = int(input('Quantos termos você gostaria de saber a mais? '))
        qtd_termo += contador
    else:
        continua = False
print('Progressão finalizada com {} termos mostrados'.format(qtd_termo))
