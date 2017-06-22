limite=int(input("Informe um valor máximo de linhas para a construção da sequência de Fibonacci: "))
saida=0
saida1=0
saida2=1
contador=1
while contador<=limite:
  saida=saida1+saida2
  print(saida)
  contador=1+contador
  saida2=saida1
  saida1=saida
