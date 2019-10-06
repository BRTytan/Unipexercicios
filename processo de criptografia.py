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


#METODO PARA DEFINIR D
def defineD(phiN,e):
    d = 0
    d = d * e 
    while(d%phiN):
        d += 1
    return d


def mod(a,b):
    if(a<b):
        return a
    else:
        c=a%b
        return c


def private_key(toti, e):
    d = 0
    while(mod(d*e, toti)!=1):
        d +=1
    return d


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


#################################### criação da chave privada ############################

d = private_key(phiN,e)


################################### criptografando texto ##############################


texto = input("Informe um texto: ")

lista = []
listacrip = []
for caracter in texto:

    asc = ord(caracter)
    num = asc ** e
    listacrip.append(mod(num, n))
    lista.append(caracter)
   


################################### descriptografando texto ###############################33


indice = 0
listadescrip = []
listaAsc = []

for letra in listacrip:
    caracter = listacrip[indice]
    result = caracter ** d
    valor = mod(result, n)
    listaAsc.append(valor)
    listadescrip.append(chr(valor))
    indice += 1


print("")
print("Primeiro número aleatorio P: " + str(p))
print("Segundo número aleatorio Q: " + str(q))
print("")
print("Chave E: " + str(e))
print("Chave N: " + str(n))
print("Esse é o phiN de N: " + str(phiN))
print("Chave D: " + str(d))

print("")

print("Texto que foi criptografada: " + '\033[32m'+ texto +'\033[0;0m' )

print("")

print("Essa é a lista criptografada: ") 
print(listacrip)

print("")

print("Essa é a lista ASC, faz parte do processo de descriptografia: ")
print(listaAsc)

print("")

print("Essa é a lista descriptografada: ")
print(listadescrip)


