nota1=int(input("Digite primeira nota: "))
nota2=int(input("Digite segunda nota: "))
nota3=int(input("Digite terceira nota: "))
nota4=int(input("Digite quarta nota: "))
media=(nota1+nota2+nota3+nota4)/4
print(media)
if media>9:
    print("Ótimo")
else:
    if media>7:
        print("Bom")
    else:
        if media>6:
            print("Suficiente")
        else:
            print("Insuficiente")

