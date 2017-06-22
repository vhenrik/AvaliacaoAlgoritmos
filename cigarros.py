cig_fum=int(input("Informe quantos cigarros são fumados por dia: "))
anos_fum=int(input("Há quantos anos você fuma?: "))
med_p=cig_fum*10
por_d=med_p/1440
dias_p=por_d*365*anos_fum
print("Você já perdeu %d dias de vida. Pare de fumar!" %(dias_p))
