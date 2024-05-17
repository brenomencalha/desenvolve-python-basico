#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n

import random
import math

soma_int = 0

n = int(input("Digite a quantidade de números a serem testados: "))

for i in range (0, n):
    inteiro = random.randint (0,100)
    soma_int += inteiro

print (f"A raiz da soma dos valores é: {math.sqrt(soma_int)}")

