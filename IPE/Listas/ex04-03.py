'''
Exercicio 04-03:Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
'''

count = 10
print('Contagem regressiva')

while count >= 0:
    print(count)
    count -= 1

print('fogo!')
