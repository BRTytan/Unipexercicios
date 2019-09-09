"""
Exercicio 02-10: Faça um programa que calcule o aumento de um salário. Ele deve solicitar o
valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""
salario = float(input('Digite seu salário: '))
porcent = float(input('quantos porcento de aumento você recebeu? '))
calculo = (salario * porcent) / 100
print(f'seu salário atual é R${salario:.2f} e você recebeu um aumento de R${calculo:.2f} \nseu novo salário será de R${calculo+salario:.2f}')
