"""
Exercicio 15:Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ela já fumou. Considere
que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um
fumante perderá. Exiba o total em dias.
"""
import math
cigarros = int(input('Quantos cigarros por dia, você fuma? '))
ano = int(input('Em quantos anos você ja fumou? '))
vida = (ano * cigarros) / 144

print('você perdeu {} dias de vida'.format(math.trunc(vida)))