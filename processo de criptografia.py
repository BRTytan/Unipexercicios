from random import *

#MÉTODO PARA VERIFICAR SE O NÚMERO E PRIMO
def primo(num):
  c = 1 
  cont = 0 
  while c <= num:
    if num % c == 0:
      cont += 1
      c += 1
    else:
      c += 1

  if cont == 2:
    return True #RETORNA TRUE SE FOR UM NÚMERO PRIMO!
  else:
    return False

################################### CRIAÇÃO DA CHAVE PUBLICA ##############################################################
aux = False   

while aux == False:   #gera dois números aleatorios até que os dois sejam primos
  p = randint(1,100)
  q = randint(1,100)
  if primo(p) and primo(q):
    aux = True
  else:
    aux = False

#P e Q já são números primos, então já é possivel calcular o phi de N
n = p * q
phiN = (p-1) * (q-1)

#A variavel ""E"" deve ser um número primo e maior que 1 e menor que phiN
aux1 = False

while aux1 == False:
  e = randint(1,phiN) #gera um número aleatorio, entre 1 e phiN

  if primo(e): #verifica se o número gerado é primo
    aux1 = True


print("Esse é o numero E: " + str(e))
print("Esse é o número N: " + str(n))
print("Esse é o phiN: " + str(phiN))
print("Primeiro número P: " + str(p))
print("Segundo número Q: " + str(q))
