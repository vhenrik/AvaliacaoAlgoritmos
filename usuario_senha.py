'''2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''
n=(input("Informe um nome de usuário: "))
x=(input("Informe uma senha diferente do usuário: "))
b=(1)
while b==1:
    if n==x:
        print("Usuário informado é igual a senha.")
        x=(input("Informe uma senha diferente do número de usuário: "))
    else:
        b=b-1
    print("Usuário e senha corretos.")
