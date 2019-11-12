"""
Exercicio 03-01: Escreva um programa no qual leia dois valores numéricos e imprima o maior deles.
Caso ambos os números forem iguais, imprima na tela “números iguais”.
"""

n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')

if n1 > n2:
    print(f'O maior valor é {n1}')
elif n2 > n1:
    print(f'O maior valor é {n2}')
else:
    print('Os numeros são iguais')