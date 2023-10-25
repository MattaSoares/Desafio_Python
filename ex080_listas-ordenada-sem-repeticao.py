# Desafio 080 - Listas: Ordenada sem repetições
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
valores = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(n)
        print('Primeiro item da lista')
    else:
        if n > max(valores):
            valores.append(n)
            print('Adicionado ao FINAL da lista')
        elif n < min(valores):
            valores.insert(0, n)
            print('Adicionado no COMEÇO da lista')
        else:
            if n < valores[1]:
                valores.insert(1, n)
                print('Valor adicionado na segunda posição da lista')
            elif n < valores[2]:
                valores.insert(2, n)
                print('Valor adicionado no meio da lista')
            elif n < valores[3]:
                valores.insert(3, n)
                print('Valor adicionado na penúltima posição da lista')
print(valores)
