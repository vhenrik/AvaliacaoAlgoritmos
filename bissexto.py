'''Determine se um ano é bissexto:
para ser bissexto, o ano deve ser:
	Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
	Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
	Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.'''
ano=int(input('Informe um ano: '))
if (ano % 4)==0:
   print("O ano informado é bissexto.")
else:
   print('O ano informado não é um ano bissexto.')
