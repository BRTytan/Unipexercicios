"""
Exercicio 03-02:Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso,
exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h.
"""
resposta = input('deseja saber se foi multado ou não? "s" para sim e "n" para não ')
if resposta == 's' or 'S':
    velocidade = float(input('Qual a velocidade do carro?'))
    multa = float(velocidade + 5) - 80
    print(f'sua velocidade é {velocidade}km/h, portanto você deve pagar R${multa} de multa')
elif resposta == 'n' or 'N':
    print('Tenha um Bom-dia')