# Desafio 092 - Cadastro de funcionario
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionario receberá também o ano de contratação e o salario.
# Calcule e acrescente, além da idade, com quantos asnos a pessoa vai se aposentar.
# Obs: Considere 35 anos de contribuição
from datetime import date

cadastro = {}
while True:
    cadastro['nome'] = str(input('Nome: '))
    ano_nascimento = int(input('Ano de Nascimento: '))
    ano_hoje = date.today().year
    cadastro['idade'] = ano_hoje - ano_nascimento
    cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if cadastro['ctps'] == 0:
        break
    cadastro['contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (cadastro['contratacao'] + 35) - ano_nascimento
    break
print('-' * 30)
for key, value in cadastro.items():
    print(f'{key} tem o valor {value}')
