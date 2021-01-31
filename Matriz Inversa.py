#Código criado por: Iury Chagas da Silva Caetano
import numpy as np
#importando a biblioteca numpy

#exibindo mensagem da funcionalidade do programa
print("Este programa mostra a inversa da matriz Anxn digitada! \n")
# por se tratar de uma matriz invertivel, assume-se que ela é uma matriz quadrada, por tanto, não há necessidade de pedir linhas e colunas separadamente, e sim apenas a quantidade de linhas
Linha = int(input("Insira a quantidade de linhas da matriz!\n"))
Coluna = Linha

#definindo uma matriz do tamanho requisitado, entretanto com lixo de memoria, pois será substituido pelos dados que o usuaŕio inserir
A = np.empty([Linha, Coluna], dtype = float)

#processo de incremento dos dados na matriz
for i in range (0,Linha):
  for j in range (0,Coluna):
    A[i][j] = float(input("Digite o elemento [{}] [{}] da matriz A: ".format (i,j)))
#fazendo a inversa da matriz:
print("A matriz A digitada: \n{}".format (A))

#o metodo linalg.pinv(A) faz a inversa da matriz, recurso este, presente na biblioteca numpy
print("A matriz inversa de A: \n {}".format (np.linalg.pinv(A)))


