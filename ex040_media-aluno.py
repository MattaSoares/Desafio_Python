# Desafio 040 - Media aluno
# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[31mReprovado.\033[m Sua média foi de {:.1f}'. format(media))
elif media >= 5.0 and media <= 6.9:
    print('\033[33mRecuperação.\033[m Sua média foi de {:.1f}'.format(media))
else:
    print('\033[32mAprovado.\033[m Sua média foi de {:.1f}'. format(media))
