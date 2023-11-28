def leiaDinheiro(prompt):
    while True:
        valor = str(input(prompt)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mErro: "{valor}" é um preço inválido!\033[m')
        else:
            return float(valor)

