#Código criado por: Iury Chagas da Silva Caetano
import numpy as np #importando bibliteca numpy para o objeto np

#variaveis com inicialização em 0 para retirar lixo de memoria
identidade = 0
simetrica = 0
antisimetrica = 0
nula = 0
#solicitando ao usuario os dados necessarios
print("##### Este programa identifica a matriz digitada e informa o seu tipo! ####### \n")
Coluna = int(input("Digita o valor da coluna da matriz: \n"))

Linha = int(input("Digita o valor da linha da matriz: \n"))
#inicializando uma matriz com lixo de memoria, porem em mesma proporção digitada pelo usuario
M = np.empty([Linha, Coluna], dtype = float)
#implementando os valores a matriz
for i in range(0, Linha):
    for j in range(0, Coluna):
      M[i][j] = float(input("Digite o elemento [{}][{}] da matriz A: ".format(i,j)))

print(" A Matriz fornecida: M \n{}".format(M))
#comparando matriz indentidade com matriz digitada
for l in range(0,Linha):
  for m in range(0,Coluna):
    I = np.eye(Coluna)
    if M[l,m] == I[l,m]:
      identidade += 1
    if M[l,m] != I[l,m]:
      identidade = 0
      
if identidade == Linha*Coluna:
  resultado = 1;
  print("\nÉ matriz identidade\n")
#definindo matriz simetrica a partir da definição
for s in range(0,Linha):
  for t in range(0,Coluna):
    if M[s,t] == M[t,s]:
      simetrica +=1
if simetrica == Coluna*Coluna:
  print("\nÉ simetrica\n")
#definindo matriz anti simetrica a partir da definição
for a in range(0,Linha):
  for b in range(0,Coluna):
    if M[a,b] == - M[a,b] and M[a,a] == 0:
      antisimetrica +=1
if antisimetrica == Coluna:
  print("\nÉ antisimetrica\n")

#inicializando matriz nula e comparando-a com a matriz fornecida
for c in range(0,Linha):
  for d in range(0,Coluna):
    Z = np.zeros((Linha, Coluna))
    if M[c,d] == Z[c,d]:
      nula += 1
    if M[c,d] != Z[c,d]:
      nula = 0
      
if nula == Linha*Coluna:
  print("\nÉ matriz nula\n")
#condição para determinar a matriz como um tipo desconhecido
if identidade != Linha*Coluna and simetrica != Coluna*Coluna and antisimetrica != Coluna and nula != Linha*Coluna:
  print("\nA matriz M é de um tipo desconhecido: \n{}".format(M))
