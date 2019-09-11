"""
Exercicio 02-11: Faça um programa solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""

print('deseja saber o preço da mercadoria?\n')
valor = str(input('Digite "s" para sim e "n" para não: '))

if valor == 's' and 'S':
        preço = float(input('Digite o valor do produto: '))
        if preço >= 50:
            preço = float(input('Digite o valor do produto: '))
            print('seu desconto é de 15%')
            print(f'o valor do produto é R${preço:.2f}, com desconto de 15% é')
            print(f'R${preço-(preço*15/100):.2f}')
        else:
            print(f'seu desconto é de 10% \nSendo assim seu produto do valor R${preço:.2f}, com desconto de 10% é')
            print(f'R${preço-(preço*10/100):.2f}')
elif valor == 'n' and 'N':
    print('Tenha um bom-dia')
else:
    print('você digitou algo errado')
