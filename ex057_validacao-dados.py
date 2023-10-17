# Desafio 057 - Validação de Dados
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o seu Sexo: [M/F] ')).upper().strip()[0]
print(sexo)
while sexo not in 'MF':
    sexo = str(input('Valor incorreto. Digite o sexo com "M" para masculino e "F" para femnino: [M/F] ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
