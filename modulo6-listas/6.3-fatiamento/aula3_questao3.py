import random

# Passo 1: Gerar a lista de 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Função para encontrar o intervalo com a maior quantidade de números negativos
def encontrar_intervalo_negativos(lista):
    max_negativos = 0
    inicio_intervalo = 0
    fim_intervalo = 0

    for i in range(len(lista)):
        for j in range(i+1, len(lista)+1):
            sub_lista = lista[i:j]
            negativos = sum(1 for x in sub_lista if x < 0)
            if negativos > max_negativos:
                max_negativos = negativos
                inicio_intervalo = i
                fim_intervalo = j

    return inicio_intervalo, fim_intervalo

# Imprimir a lista original
print("Lista original:", lista)

# Passo 2: Encontrar o intervalo com a maior quantidade de números negativos
inicio, fim = encontrar_intervalo_negativos(lista)

# Passo 3: Deletar o intervalo encontrado
del lista[inicio:fim]

# Imprimir a lista depois da deleção
print("Lista após a deleção:", lista)
