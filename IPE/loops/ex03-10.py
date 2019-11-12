'''Exercicio 03-10: Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencial,
I para industrial e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir:
• Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.
• Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.
• Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60.
'''

energiaEletrica = int(input('Qual a quantidade de kWH consumida?'))
tipoInstalação = input('Escolha uma das opções "R" residencial, "I" industrial ou "C" Comercial: ')
resultado = 0
if tipoInstalação == "R" or "r" and energiaEletrica <= 500:
    resultado = energiaEletrica * 0.40
    print(resultado)
elif energiaEletrica > 500:
    resultado = energiaEletrica * 0.65
    print(resultado)
elif tipoInstalação == "I" or "i" and energiaEletrica <= 1000:
    resultado = energiaEletrica * 0.55
    print(resultado)
elif energiaEletrica > 1000:
    resultado = energiaEletrica * 0.60
    print(resultado)
elif tipoInstalação == "C" or "c" and energiaEletrica < 5000:
    resultado = energiaEletrica * 0.55
    print(resultado)
elif energiaEletrica > 5000:
    resultado = energiaEletrica * 0.60
    print(resultado)

