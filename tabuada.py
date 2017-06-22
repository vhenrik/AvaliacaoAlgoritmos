n=int(input("Informe um número para consulta de tabuada: "))
b=int(input("Informe um número limite para a sua tabuada(Ex: Tabuada até 10): "))
i=0
while i<b+1:
	x=i*n
	print("%d x %d = %d"%(i,n,x))
	i=i+1
