valor_produto=int(input('Informe o valor do produto: '))

valor_pago=int(input('Informe o valor entregue para pagamento: '))

troco=valor_pago - valor_produto

if troco > 0:

  print('Seu troco é de: R$ %s .'%(troco))

  for p in 100, 50, 20, 10, 5, 2, 1:

      if troco >= p:

          n = int(troco/p)

          r = troco - p * n

          print ('%s nota(s) de R$ %s'%(n, p))

          troco = r

else:

  print ('A quantia entregue é menor que o valor do produto.')
