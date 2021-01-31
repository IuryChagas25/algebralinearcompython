#Código criado por: Iury Chagas da Silva Caetano

import numpy  as np #importando a biblioteca numpy para o objeto "np"

#definindo uma matriz, onde cada indice desse array, será feito uma linha da matriz

A = np.array([[1,3,4,5],[2,5,6,7],[5,6,3,2]])

print("Vamos escalonar a matriz: \n{}".format(A))
print("\nEscalonando: \n")
#Fazendo o processo de escalonamento matricial manualmente
A[1,0:3] = -2*A[0,0:3] + A[1,0:3]
print("{}".format(A))
A[2,0:3] = -5*A[0,0:3] + A[2,0:3]
print("\n{}".format(A))
A[1,0:3] = -A[1,0:3]
A[2,0:3] = 9*A[1,0:3] + A[2,0:3]
print("\n{}".format(A))

#informando as dimensões da matriz A
print(A.shape)
