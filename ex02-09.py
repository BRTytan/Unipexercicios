"""
Exercicio 02-09:Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.
"""
print('digite a baixo os dias, horas, minutos e segundos para receber o total em segundos')
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
calculo = (dias*86400)+(horas*3600)+(minutos*60)

print(f'o resultado de {dias}d, {horas}h, {minutos}m, {segundos}s é: {calculo}')
