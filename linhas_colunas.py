'''Faça um algoritmo que o usuário informe a quantidade de linhas e colunas que a matriz deve ter.'''
linhas=int(input("Quantidade de linhas: "))
colunas=int(input("Quantidade de colunas: "))
matriz = [0]*linhas
for i in range(linhas):
   matriz[i] = [0]*colunas
print(matriz)
