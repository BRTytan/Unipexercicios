"""
Exercicio 03-03: Escreva um programa que leia três números e que imprima o maior e o menor.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n3 > n2:
    print(f'o número maior é {n1} e o número menor é {n2}')
if n2 > n1 and n3 > n1:
    print(f'o número maior é {n2} e o número menor é {n1}')
elif n3 > n1 and n1 > n2:
    print(f'o número maior é {n3} e o número menor é {n1}')
else:
    print(f'o número maior é {n3} e o número menor é {n2}')