"""
Exercicio 03-08:Escreva um programa que leia dois números e que pergunte qual operação você deseja
realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada.
"""
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
escolha = input('Digite um sinal(+, -, * ou /) para calcular os valores digitados anteriormente: ')

if escolha == '+':
    resultado = n1 + n2
    print(f'você escolheu a adição: {n1} + {n2} = {resultado}')
elif escolha == '-':
    resultado = n1 - n2
    print(f'você escolheu subtração: {n1} - {n2} = {resultado}')
elif escolha == '*':
    resultado = n1 * n2
    print(f'você escolheu multiplicação: {n1} X {n2} = {resultado}')
elif escolha == '/':
    resultado = n1 / n2
    print(f'você escolheu divisão: {n1} / {n2} = {resultado}')
else:
    print('você digitou o sinal incorreto tente novamente')