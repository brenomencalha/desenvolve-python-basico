import random

# construção das duas listas com valores aleatórios

aleatorios_1 = []
aleatorios_2 = []

for i in range (20):
    valores_1 = (random.randint (0,50))
    aleatorios_1.append (valores_1)

    valores_2 = random.randint (0,50)
    aleatorios_2.append (valores_2)
   
# imprime as duas listas geradas:
print (f'Primeira lista: {aleatorios_1}')
print (f'Segunda lista: {aleatorios_2}')

# criação da terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas:
    
intersec = []

for elemento in aleatorios_1:
    if elemento in aleatorios_2 and elemento not in intersec:
        intersec.append (elemento)

intersec.sort()

print(f'Lista "intersecção" ordenada: {intersec}')

print("Contagem:")
for i in intersec:
    print(f'{i}: (Primeira lista: {aleatorios_1.count(i)}, Segunda lista: {aleatorios_2.count(i)})')


    
