# coding=utf-8
"""rsa
multiplicação de dois numeros primos
gerar chave assimetrica
passo 1: multiplicar dois números primos aleatorios(quanto maior, mais seguro). este número é o nosso produto ("n")
passo 2:calcular totient fi(n) = (n1-1) * (n2-1)
passo 3:escolher um npumero primo q seja maior que 1 e menor que o valor do passo 2 e precisa ser primo do totient
passo 4:calcular o "inverso multiplicativo" do valor do passo 3 em mod(resto da divisao) (phi(n))
"""
'''p = int(input("Digite um valor:"))
q = int(input("Digite outro valor: "))
e = input('qual o valor da chave pública: ') ### chave pública

product = p*q
print(f'o valor de produto é: {product}')  ### o tamanho do nosso conjunto finitor de valores###

phiDeN = (p-1) * (q-1)      ### me diz a quantidade de co-primos de um numero que são menores que ele mesmo.###
print(f'nossa função totiente é: {phiDeN}')'''

p = int(input('Digite um valor primo: '))
q = int(input('Digite outro valor primo: '))
n = p * q                                           # Tamanho do conjunto #
if n % 3 == True:
    print(f'Valor do produto é: {n}')
else:
    print('Números não são primos')
fiDeN = (p - 1) * (q - 1)                           # Função Totient #
if n % 3 == True:
    print(f'função totient do produto é: {fiDeN}')
else:
    print('Números não são validos')

e = int(input(f'Digite um número primo, que seja maior que 1 e menor que {fiDeN}: '))

            ## Calculando chave pública ##
if e <= fiDeN:
    frase = str(input('Digite uma letra para cifrar: '))
    if frase == 't' or 'T':
        frase = 19
        print(f'a letra tem o valor númerico de {frase}')
        if frase == 19:
           c = (frase ** e) % n
           print(f'sua letra cifrada é {c}')
else:
    print('Número incorreto')