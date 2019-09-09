"""
Exercicio 08: Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
1 metro é igual a 100 cm que é igual a 1000 mm.
"""
valor = float(input('Digite quantos metros você precisa para a conversão: '))
converter = valor * 1000
print('o valor em {}m convertido em milimetros é {}mm'.format(valor, converter))