'''Exercício 2:crie um algoritmo que solicite 3 valores que representarão os lados de um triângulo. Considere que não importa a ordem que serão fornecidos os valores, podendo ser fornecido primeiro a hipotenusa e depois os catetos, ou primeiro os catetos e depois a hipotenusa, etc.'''
import math

def triangret(vet):
    if vet[0] > vet[1] and vet[0] > vet[2]:
        hip = vet[0]
        cat1 = vet[1]
        cat2 = vet[2]
    elif vet[1] > vet[0] and vet[1] > vet[2]:
        hip = vet[1]
        cat1 = vet[0]
        cat2 = vet[2]
    else:
        hip = vet[2]
        cat1 = vet[0]
        cat2 = vet[1]
        print (hip, cat1, cat2b lgeb)

    if hip == math.sqrt(cat1**2 + cat2**2):
        return 1
    else:
        return 0

vet = [0]*3
for i in range(3):
    vet[i] = input('Digite um valor: ')

if triangret(vet) == 1:
    print 'É retangulo'
else:
    print 'Não é retangulo'
