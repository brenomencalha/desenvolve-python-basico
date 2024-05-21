def substituir_vogais(frase):
    # Definindo as vogais (tanto maiúsculas quanto minúsculas)
    vogais = "aeiouAEIOU"
    
    # Substituindo cada vogal por '*'
    frase_modificada = ''.join('*' if char in vogais else char for char in frase)
    
    return frase_modificada

# Solicita uma frase ao usuário
frase_usuario = input("Digite uma frase: ")

# Chama a função para substituir as vogais
frase_modificada = substituir_vogais(frase_usuario)

# Imprime a frase modificada
print("Frase modificada:", frase_modificada)
