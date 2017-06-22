print("A proposição 'pv(q^r)<-->(pvq)^(pvr)' será solucionada de acordo com os valores das variáveis 'p' 'q' e 'r' que você informar.")
print('')
print("Legenda:\n '^'-Conjunção(ex:e) \n 'v'-Disjunção(ex:ou) \n '-->'-Condicional(ex:então) \n '<-->'-Bicondicional(ex:se somente se)")
print('')
rept=1
cont=1
while cont==1:
	p=(input("Informe um valor('v' para verdade ou 'f' para falso) para a variável 'p': "))
	q=(input("Informe um valor('v' para verdade ou 'f' para falso) para a variável 'q': "))
	r=(input("Informe um valor('v' para verdade ou 'f' para falso) para a variável 'r': "))
	print('')
	print('--------------------------------------------------------------------------------------------------------------------------------------------')
	print('')


	print("Resolução da proposição: ")
	if p=='v' and q=='v' and r=='v':
	    print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nv   v   v     v       v       v        v           v                 v")
	    if p=='v' and q=='v' and r=='f':
	        print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nv   v   f     f       v       v        v           v                 v")
	    if p=='v' and q=='f' and r=='f':
	        print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nv   f   f     f       v       v        v           v                 v")
	    if p=='f' and q=='v' and r=='v':
	        print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nf   v   v     v       v       v        v           v                 v")
	    if p=='f' and q=='f' and r=='v':
	        print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nf   f   v     f       f       v        f           f                 v")
	    if p=='v' and q=='f' and r=='v':
	        print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nv   f   v     f       v       v        v           v                 v")
	    if p=='f' and q=='v' and r=='f':
	        print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nf   v   f     f       v       f        f           f                 v")
	    if p=='f' and q=='f' and r=='f':
	        print("p   q   r   (q^r)   (pvq)   (pvr)   pv(q^r)   (pvq)^(pvr)   pv(q^r)<-->(pvq)^(pvr)\nf   f   f     f       f       f        f           f                 v")
	    cont=0
	x=(input("\n\nDeseja realizar nova operação?('sim' ou 'não'): "))
	if x=='sim':
	    cont=1
	else:
	    cont=0
