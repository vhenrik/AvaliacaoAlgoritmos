'''Utilizando a estrutura SE SENÃO, faça um algoritmo que deve possuir uma variável do tipo inteiro o ano de nascimento e a subtração pelo ano atual for menor que 18 informar a mensagem: "MENOR DE IDADE".'''
ano_nascimento=int(input("Informe o seu ano de nascimento: "))
ano_atual=int(input("Informe o ano atual: "))
idade=ano_atual-ano_nascimento
if idade<18:
   print ("Você é menor de idade")
else:
   print("Você é maior de idade")
