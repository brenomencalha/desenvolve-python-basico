from itertools import permutations

def encontrar_anagramas(string, palavra_objetivo):
    anagramas = set()  # Usaremos um conjunto para garantir que não haja duplicatas
    string = string.lower()

    # Gerar todos os anagramas da palavra objetivo
    perms = [''.join(p) for p in permutations(palavra_objetivo)]

    # Verificar se cada anagrama está presente na string
    for perm in perms:
        if perm in string:
            anagramas.add(perm)

    return anagramas

#inputs
string = input("Digite uma frase:")
palavra_objetivo = input("Palavra objetivo: ")
resultado = encontrar_anagramas(string, palavra_objetivo)
print("Anagramas encontrados:", resultado)
