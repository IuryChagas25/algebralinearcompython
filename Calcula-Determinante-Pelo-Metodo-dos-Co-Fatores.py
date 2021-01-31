#Código criado por: Iury Chagas da Silva Caetano
import numpy as np
#importando bibliotena numpy ao obejeto "np"

print("Insira uma matriz quadrada para calcular seu determinante! \n")
Linha = int(input("Insira a dimensão da Matriz: "))
Coluna = Linha
#gerando uma matriz com lixo de memoria, mas com as dimensões inseridas
M = np.empty([Linha,Coluna], dtype = float)
#preenchendo a matriz
for i in range(0, Linha):
    for j in range(0, Coluna):
      M[i][j] = float(input("Digite o elemento [{}][{}] da matriz M: ".format(i,j)))
      
#definindo as submatrizez
total = 0
k=0
while k <= Linha-1:
  #Eliminando a coluna definida por "k" da matriz
  sub = (np.delete(M,k,axis = 1))
  #Eliminando a 1 linha da matriz (fixo, pois i = 1 linha)
  sub = (np.delete(sub,0,axis = 0))
  #fazendo a formula: Anxm . (-1)^n+m
  elemento1linha = M[0,k]*(-1)**k
  total = np.linalg.det(sub)*elemento1linha + total
  #contador
  k = k+1
    
print(" A Matriz fornecida:\n{}".format(M))
print(" Determinante da Matriz: \n{}".format(total))

  
