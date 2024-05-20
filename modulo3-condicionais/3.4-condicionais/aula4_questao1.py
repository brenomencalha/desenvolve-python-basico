# Problema : criar um programa que lê a soma de dois números e informa ao usuário se o resultado é par ou ímpar.

#entrada :

num1 = int(input("Digite um número inteiro qualquer: "))
num2 = int(input("Digite outro número inteiro qualquer: "))

#processamento
soma = num1 + num2

#saída
if soma % 2 == 0:
    print ("A soma dos números informados é par!")
else:
    print ("A soma dos números informados é ímpar!")

