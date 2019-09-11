"""
Exercicio 05: Calcule o resultado da expressão A > B and C or D, utilizando os valores a
seguir e após, confirme programando o resultado.
a) A = 1, B = 2, C = True, D = False
b) A = 10, B = 3, C = False, D = False
c) A = 5, B = 1, C = True, D = True
"""
opção = str(input('Digite uma opção a, b ou c: '))
if opção == 'a' or 'A':
    um: int = 1
    dois: int = 2
    tres = True
    quatro = False
    expressão = um > dois and tres or quatro
    print(f"a) A = 1, B = 2, C = True, D = False ")
    print(f" a expressão é: {expressão}")
elif opção == 'b' or 'B':
        um: int = 10
        dois: int = 3
        tres = False
        quatro = False
        expressão = um > dois and tres or quatro
        print(f"b) A = 10, B = 3, C = False, D = False ")
        print(f" a expressão é: {expressão}")
elif opção == 'c' or 'C':
        um: int = 5
        dois: int = 1
        tres = True
        quatro = True
        expressão = um > dois and tres or quatro
        print(f"c) A = 5, B = 1, C = True, D = True ")
        print(f" a expressão é: {expressão}")
else:
    print('o Valor informado não é valido')