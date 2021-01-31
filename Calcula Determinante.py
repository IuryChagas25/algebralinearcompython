#Código criado por: Iury Chagas da Silva Caetano
import numpy as np #importando biblioteca numpy para o objeto "np"

print("Insira uma matriz 3x3 para calcular seu determinante! \n")
Linha = 3
Coluna = 3
#gerando uma matriz com lixo de memoria, mas com as dimensões 3x3
M = np.empty([Linha,Coluna], dtype = float)
linha = 2
coluna = 2
subM2 = np.empty([linha,coluna])
for i in range(0, Linha):
    for j in range(0, Coluna):
      M[i][j] = float(input("Digite o elemento [{}][{}] da matriz M: ".format(i,j)))
      #fazendo a formula: Anxm . (-1)^n+m
      elemento1linha = M[0,0]*(-1)**0
      elemento2linha = M[0,1]*(-1)**1
      elemento3linha = M[0,2]*(-1)**2
      #definindo a submatriz2
      subM2[0,0] = M[1,0]
      subM2[0,1] = M[1,2]
      subM2[1,0] = M[2,0]
      subM2[1,1] = M[2,2]
      sub = (np.delete(M,j,axis=1))
      sub = (np.delete(sub,0,axis=0))
#definindo a submatriz1

subM1 = M[1:3, 1:3] 
#definindo a submatriz3
subM3 = M[1:3,0:2]
for k in range(0,linha):
  for l in range(0, coluna):
    #fazendo a formula: Anxm . (-1)^n+m
    e1linha1 = subM1[0,0]*(-1)**0
    e2linha1 = subM1 [0,1]*(-1)**1
    #fazendo a submatriz 1
    primeirasubsubM1 = subM1[1,1]
    segundasubsubM1 = subM1[1,0]
    #fazendo a formula: Anxm . (-1)^n+m
    e1linha1sub2 = subM2[0,0]*(-1)**0
    e2linha1sub2 = subM1[0,1]*(-1)**1
    #fazendo a submatriz 2 
    primeirasubsubM2 = subM2[1,1]
    segundasubsubM2 = subM2[1,0]
    #fazendo a formula: Anxm . (-1)^n+m
    e1linha1sub3 = subM3[0,0]*(-1)**0
    e2linha1sub3 = subM3[0,1]*(-1)**1
    #fazendo a submatriz 3
    primeirasubsubM3 = subM3[1,1]
    segundasubsubM3 = subM3[1,0]
#calculando os determinantes    
detM1 = elemento1linha *(e1linha1*primeirasubsubM1+e2linha1*segundasubsubM1)
detM2 = elemento2linha *(e1linha1sub2*primeirasubsubM2+e2linha1sub2*segundasubsubM2)
detM3 = elemento3linha *(e1linha1sub3*primeirasubsubM3+e2linha1sub3*segundasubsubM3)

##Outra forma de calcular o determinante:
##detM1 = elemento1linha*(subM1[0,0] * subM1[1,1] - subM1[0,1]*subM1[1,0])
##detM2 = elemento2linha*(subM2[0,0] * subM2[1,1] - subM2[0,1]*subM2[1,0])
##detM3 = elemento3linha*(subM3[0,0] * subM3[1,1] - subM3[0,1]*subM3[1,0])

print(" A Matriz fornecida:\n{}".format(M))
#Exibir as submatrizes existentes:
print(" Sub matriz 1\n{}".format(sub))
#print(" Sub matriz 2 \n{}".format(subM2))
#print(" Sub matriz 3 \n{}".format(subM3))
##print(" Elemento a11 \n{}".format(elemento1linha))
##print(" Elemento a12 \n{}".format(elemento2linha))
##print(" Elemento a13 \n{}".format(elemento3linha))
print("Determinante da Matriz M:\n {}".format (detM1+detM2+detM3))