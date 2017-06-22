def troca(vet):
    for i in range(3):
        if vet[i]== 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet
    vet=[]
cont=0
while cont<3:
    x=int(input("Informe um valor para a posição %d: "%(cont+1)))
    vet.append(x)
cont+=1
print(vet)
troca(vet)
