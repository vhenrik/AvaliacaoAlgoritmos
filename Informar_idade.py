d_nasc=input("Informe a data de nascimento [dd/mm/aaaa] -> ")

d_atual=input("Informe a data atual [dd/mm/aaaa] -> ")

dia_nasc=int((d_nasc[0:2]))
mes_nasc=int((d_nasc[3:5]))
ano_nasc=int((d_nasc[6:10]))

dia_atual=int((d_atual[0:2]))
mes_atual=int((d_atual[3:5]))
ano_atual=int((d_atual[6:10]))

if(mes_atual>=mes_nasc):
   if(dia_atual>=dia_nasc):
       idade=ano_atual-ano_nasc
       print(idade)
else:
   idade=ano_atual-ano_nasc-1
   print(idade)
