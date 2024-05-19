#Escreva um script python que use compreensão de listas para criar as seguintes listas:

# - Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
# - Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
# - Todos os números entre 1 e 100 que sejam divisíveis por 7
# - Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 

# lista em que os números pares serão testados:
list_main = []
for i in range (20, 51):
    list_main.append (i)
print(f'Lista principal: {list_main}')

lista_pares = [n for n in list_main if n % 2 == 0]
print (f'Lista pares: {lista_pares}')
print("\n")

# lista quadrados:
list_2 = []
for i in range (1, 10):
    list_2.append (i)
print(f'Lista principal: {list_2}')

lista_quadrado = [n**2 for n in list_2]
print(f'Lista elevada ao quadrado: {lista_quadrado}')
print("\n")

# Números entre 1 e 100 que sejam divisíveis por 7:
list_3 = []
for i in range (1, 101):
    list_3.append(i)
print(f'Lista principal: {list_3}')

lista_divisivel_7 = [n for n in list_3 if n % 7 == 0]
print(f'Lista divisível por sete: {lista_divisivel_7}')
print("\n")

# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento:
list_4 = []
for i in range (0, 30, 3):
    list_4.append(i)
print(f'Lista principal: {list_4}')

lista_paridade = ["Par" if n % 2 == 0 else "Ímpar" for n in list_4]
print(f'Lista paridade: {lista_paridade}')
print("\n")