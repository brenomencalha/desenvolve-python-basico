def contar_espacos (frase):
    contador = 0
    for caractere in frase:
        if caractere == " " :
            contador += 1
    return contador

# uso da função contar_espacos
frase = input("Digite uma frase: ")

num_espacos = contar_espacos (frase)
print (f'Espaços em branco: {num_espacos}')