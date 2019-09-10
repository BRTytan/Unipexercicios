"""
Exercicio 06: Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa
apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis:
materia1, materia2, materia3.
"""

ma1 = float(input('qual sua primeira nota: '))
ma2 = float(input('qual sua segunda nota: '))
ma3 = float(input('qual sua terceira nota: '))

if ma1 >= 7 and ma2 >= 7 and ma3 >= 7:
    print('1° {}, 2° {} e 3° {} você obteve nota a cima de 7 em todas, portanto você passou!!'.format(ma1, ma2, ma3))
else:
    print('você foi reprovado')