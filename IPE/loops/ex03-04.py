"""
Exercicio 03-04: Escreve um programa que pergunte o salário do funcionário e calcule o valor
do aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores
ou iguais, de 15%.
"""

salario = float(input('Qual seu salário? '))
if salario <= 1250:
    resultado = (salario*15/100)+salario
    print(f'seu salario anterior é R${salario:.2f} e seu salário atual é R${resultado:.2f}')
else:
    resultado = (salario*10/100)+salario
    print(f'seu salário anterior é R${salario:.2f} e seu salário atual é R${resultado:.2f}')