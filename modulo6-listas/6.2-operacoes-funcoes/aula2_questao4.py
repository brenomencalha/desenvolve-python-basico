#  Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

# define a quantidade de elementos e adiciona os inputs de tais elementos a primeira lista:
n1 = int(input("Digite a quantidade de elementos da primeira lista:"))

lista_1 = []

print("Digite os elementos da primeira lista: ")

for i in range (n1):
    elementos_list_1 = int(input())
    lista_1.append(elementos_list_1)
print(lista_1)

# define a quantidade de elementos e adiciona os inputs de tais elementos a segunda lista:

n2 = int(input("Digite a quantidade de elementos da segunda lista:"))

lista_2 = []

print ("Digite os elementos da segunda lista:")

for i in range (n2):
    elementos_list_2 = int(input())
    lista_2.append(elementos_list_2)
print(lista_2)

# cria a terceira lista que contém os valores da lista 1 e da lista 2 alternados:

lista_3 = []

for index in range (len(lista_1)):
    lista_3.append(lista_1[index])
    lista_3.append(lista_2[index])

print(f'Lista intercalada: {lista_3}')