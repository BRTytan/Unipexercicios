"""
Exercicio 03-06: Escreva um programa que pergunte a distância que um passageiro deseja percorrer
em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45
para viagens mais longas.
"""

distancia = int(input('Qual a distancia a ser percorrida para a viagem? '))

if distancia <= 200:
    resultado = distancia*0.5
    print(f'sua distancia é: {distancia} e está a baixo de 200km, sua taxa será de R$0,50, portanto, a viagem custará R${resultado:.2f}')
else:
    resultado = distancia*0.45
    print(f'sua viagem é mais longa portanto a taxa será de R$0,45 e sua viagem custará R${resultado}')