'''5) o sistema deve perguntar a medida dos 3 lados de um triangulo, o sistema deve informar o tipo de triangulo: equilatero, isosceles ou escaleno.'''
x=0
m=[]
while x<3:
   m.append(input("Informe a valor do lado do triângulo: %d " %(x+1)))
   x=x+1
if (m[0] == m[1]) & (m[1] == m[2]):
   print("O valor informado é de um triângulo equilátero.")
elif m[0]!=m[1]!=m[2]:
   print("O valor informado é de um triângulo escaleno.")
else:
   print("O valor informado é de um triângulo isósceles.")
