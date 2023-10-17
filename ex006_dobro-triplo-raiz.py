# Desafio 006 - Dobro, Triplo, Raíz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um valor: '))
print(' O dobro do número {} é: {} \n O triplo do número {} é: {} \n A raiz quadrada do número {} é: {:.2f}'.format(num, (num * 2), num, (num * 3), num, (num ** (1/2))))
