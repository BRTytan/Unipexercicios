"""exercicio 06: Escreva o programa que receba o valor do salario, do aumento(%) e calcule
o valor do novo salario. Considere o salario de R$ 750,00 e o aumento de 15%."""

salario = 750
aumento = salario*15/100
print('seu salário atual é R${} porém você teve um aumento de 15% \ne seu salário atualmente está em: R${}'.format(salario, (aumento+salario)))