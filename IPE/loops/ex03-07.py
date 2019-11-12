"""
Exercicio 03-07:Escreva um programa que calcular a categoria de um produto e determine o preço pela
tabela: Categoria 1 valor de R$ 10,00; Categoria 2 valor de R$ 15,00; Categoria 3 valor de
R$ 19,00; Categoria 4 valor de R$ 23,00 e Categoria 5 valor de R$ 27,00.
"""

valor = str(input('Digite um numero de 1 até 5 para saber o valor de cada produto: '))

if valor == '1':
    print('categoria 1: valor do produto é 10,00')
elif valor == '2':
    print('categoria 2: valor do produto é 15,00')
elif valor == '3':
    print('categoria 3: valor do produto é 19,00')
elif valor == '4':
    print('categoria 4: valor do produto é 23,00')
elif valor == '5':
    print('categoria 5: valor do produto é 27,00')