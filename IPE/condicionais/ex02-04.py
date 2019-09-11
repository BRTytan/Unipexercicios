"""
Exercicio 02-04: Escreva um expressão para determinar se uma pessoa deve ou não pagar imposto.
considere que pagam imposto pessoas cujo salario é maior que R$1200,00
"""
salario = float(input('Digite seu salario: R$'))

if salario >= 1200:
    print('você deve pagar imposto')
if salario <= 1199:
    print('você nao deve pagar imposto')