# gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos.
# gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos.
# imprima:
# A lista elementos;
# A soma dos valores da lista;
# A média dos valores da lista.

import random

# gera o valor aleatório que será o tamanho da lista "elementos":
num_elementos = random.randint(5, 20)
print(f'Tamanho da lista elementos: {num_elementos}')

# cria a lista "elementos" de tamanho aleatório definido pela variável num_elementos:
elementos = []

for i in range (num_elementos):
    valores = random.randint(1,10)
    elementos.append (valores)

print(f'A lista elementos contém: {elementos}')

# soma os valores da lista "elementos":
print (f'A soma dos valores da lista é: {sum(elementos)}')

# apresenta a média dos valores aleatórios da lista "elementos":
print (f'A média da lista criada é: {sum(elementos) / len(elementos):.2f}')