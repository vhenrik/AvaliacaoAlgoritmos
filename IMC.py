peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
sexo=(input("Sexo (F/M): "))

imc=peso/(altura*altura)

if sexo==('f'):
   if(imc>=27.3):
       print("Você está acima do peso ideal")
   elif(imc>=25.8):
       print("Você está marginalmente acima do peso")
   elif(imc>=19.1):
       print("Você está no peso normal")
   elif(imc<19.1):
       print("Você está abaixo do peso")
elif sexo==('m'):
   if(imc>=27.8):
       print("Você está acima do peso ideal")
   elif(imc>=26.4):
       print("Você está marginalmente acima do peso")
   elif(imc>=20.7):
       print("Você está no peso normal")
   elif(imc<20.7):
       print("Você está abaixo do peso")
