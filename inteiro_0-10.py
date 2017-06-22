'''Faça um algoritmo uma pessoa informa um número aleatório entre 0 e 10 e outra pessoa irá tentar acertar o numero.'''
n=int(input("Digite um numero de 0 a 10: "))
while n<0 or n>10:
   print ("Numero inválido")
   n=int(input("Digite uma numero: "))
if n>=0 and n<=10:
   print ("Numero válido")
