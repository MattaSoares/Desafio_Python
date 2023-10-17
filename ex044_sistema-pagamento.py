# Desafio 044 - Sistema de pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro / cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco_produto = float(input('Digite o preço do produto: R$'))
print('''Escolha a condição de pagamento:
[1] à vista em Dinheiro / Cheque
[2] à vista no Cartão
[3] Parcelado no Cartão
''')
opcao = int(input('Opção: '))
if opcao == 1:
    desconto = preco_produto - (preco_produto * 10/100)
    print('\033[32mDesconto de 10% aplicado.\033[m\nSua compra de R${:.2f} agora vai custar:\nR${:.2f}'.format(preco_produto, desconto))
elif opcao == 2:
    desconto = preco_produto - (preco_produto * 5/100)
    print('\033[32mDesconto de 5% aplicado.\033[m\nSua compra de R${:.2f} agora vai custar:\nR${:.2f}'.format(preco_produto, desconto))
elif opcao == 3:
    num_parcelas = int(input('Digite a quantidade de parcelas: '))
    if num_parcelas <= 2:
        valor_parcelas = preco_produto / num_parcelas
        print('Valor a pagar: {}x de R${:.2f} sem juros.'.format(num_parcelas, valor_parcelas))
    else:
        juros = preco_produto + (preco_produto * 20/100)
        valor_parcelas = (preco_produto + juros) / num_parcelas
        print('\033[31mJuros de 20% aplicado.\033[m\nSua compra de R${:.2f} agora vai custar:\n{}x R${:.2f}'.format(preco_produto, num_parcelas, valor_parcelas))
else:
    print('\033[31mOpção Inválida. Tente novamente.\033[m')
