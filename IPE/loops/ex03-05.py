"""
Exercicio 03-05:Execute o programa no qual o usuário entre com a idade do carro e caso o valor
seja menor ou igual a 3 anos imprima “Seu carro é novo”, caso contrario “Seu carro é velho”.
"""

idadeCarro = int(input('Digite a idade do seu carro: '))

if idadeCarro <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')