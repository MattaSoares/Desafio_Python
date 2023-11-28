def linha():
    return '-' * 40


def titulo(txt):
    print(linha())
    print(f'{txt:^40}')
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'{i+1} - \033[34m{item}\033[m')
    print(linha())
    while True:
        n = validaInt('Sua opção: ')
        if n < 1 or n > len(lista):
            print(f'\033[31mErro! O número {n} não é válido. Escolha entre as opções 1 e {len(lista)}:\033[m')
        else:
            return n


def validaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número Inteiro\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nUsuário interrompeu o programa.\033[m')
            exit()
        else:
            return n

