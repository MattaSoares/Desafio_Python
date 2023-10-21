# Desafio 076 - Tuplas: Lista de Preços
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista_produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
                  'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 50)
print(f'{"Listagem de Preços":^50}')
print('-' * 50)

for i in range(0, len(lista_produtos)):
    if i % 2 == 0:
        print(f'{lista_produtos[i]:.<40}', end='')
    else:
        print(f'R${lista_produtos[i]:>8.2f}')
