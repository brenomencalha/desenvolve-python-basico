import random

def encrypt(lista_strings):
    # Gerar um valor aleatório para a chave de criptografia
    chave = random.randint(1, 10)

    # Lista para armazenar os nomes criptografados
    nomes_criptografados = []

    # Iterar sobre cada string na lista de entrada
    for string in lista_strings:
        nome_criptografado = ""
        # Criptografar cada caractere na string
        for char in string:
            # Verificar se o caractere está dentro do intervalo visível
            if 33 <= ord(char) <= 126:
                # Criptografar o caractere somando a chave
                novo_char = chr((ord(char) - 33 + chave) % 94 + 33)
            else:
                # Se o caractere não estiver no intervalo visível, mantê-lo inalterado
                novo_char = char
            nome_criptografado += novo_char
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave

# Exemplo de uso
lista_strings = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(lista_strings)
print("Chave de criptografia:", chave)
print("Nomes criptografados:", nomes_criptografados)

