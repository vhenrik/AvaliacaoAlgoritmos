'''3) Altere o algoritmo anterior e informe a maior e menor idade.'''
x=int(input("Informe Quantas idades vai digitar? "))
cont=0
Maior=0
menor=1000
while (cont<x):
    i=int(input("Informe a idade"))
    if(i>Maior):
        Maior=i
    if(i<menor):
        menor=i
    cont=cont+1
print(Maior)
print(menor)
