#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
#A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista

import random

#lista de valores aleatórios

aleatorios = []

for i in range (20):
    valor = random.randint(-100, 100)
    aleatorios.append(valor)

print (f"Lista ordenada: {sorted(aleatorios)}")
print (f"Lista original: {aleatorios}")
print (f"O índice do maior valor da lista é: {aleatorios.index(max(aleatorios))}")
print (f"O índice do menor valor da lista é: {aleatorios.index(min(aleatorios))}")