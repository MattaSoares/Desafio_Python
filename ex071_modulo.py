def titulo(txt):
    print('=' * 40)
    print(f'{txt:^40}')
    print('=' * 40)


def menu():
    titulo('CAIXA ELETRONICO')
    return leiaInt('Digite o valor a ser sacado: R$')


def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número válido.\033[m')
        else:
            return n


def operacao(total):
    notas_disponiveis = [200, 100, 50, 20, 10, 5, 2]
    notas_cliente = list()
    for nota in notas_disponiveis:
        while True:
            if total == 6 and nota == 5:
                    break
            elif total >= nota:
                notas_cliente.append(f'R${nota}')
                total -= nota
            else:
                break
    if total == 1:
        notas_cliente.append('\033[31mR$1 - Este caixa não possui moedas.\033[m')

    return notas_cliente


def saida_notas(lista):
    from time import sleep
    titulo('Aguarde...')
    sleep(1)
    for i in range(0, len(lista)):
        print(f'\033[32m{lista[i]}\033[m')
        sleep(1)
    titulo('Volte Sempre')

