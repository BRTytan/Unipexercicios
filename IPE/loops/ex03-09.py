"""
Exercicio 03-09:Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação
como sendo o valor da casa a comprar dividido pelo numero de meses a pagar.
"""
import math
print('faça seu emprestimo agora')
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salario? '))
mesesPagar = int(input('Em quantos meses deseja pagar? '))
opcao = (salario * 30/100)+salario

if salario <= opcao:
    resultado = casa/mesesPagar
    print(f'o valor da casa é: R${casa:.2f} e sua prestação para o imóvel desejado é R${resultado:.2f}')