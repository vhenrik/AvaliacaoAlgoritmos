'''8) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''
cont = 0
vet=[]
par=[]
imp=[]
while cont<20:
	x=int(input("Informe um valor inteiro: "))
	cont = cont+1
	vet.append(x)
	if x%2 == 0:
	    par.append(x)
	else:
	    imp.append(x)
	print("Vetor de números pares e ímpares: ",vet)
	print("Vetor de números pares: ",par)
	print("Vetor de números ímpares: ",imp)
