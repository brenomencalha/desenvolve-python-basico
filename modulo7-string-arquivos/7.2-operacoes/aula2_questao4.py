import string

def normalizar_frase(frase):
    # Remove espaços em branco e pontuações, e converte para minúsculas
    frase = frase.lower()
    frase = ''.join(char for char in frase if char.isalnum())
    return frase

def verificar_palindromo(frase):
    # Normaliza a frase
    frase_normalizada = normalizar_frase(frase)
    # Verifica se a frase normalizada é igual à sua versão invertida
    return frase_normalizada == frase_normalizada[::-1]

def main():
    while True:
        # Solicita a frase do usuário
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
        
        # Verifica se o usuário deseja encerrar o programa
        if frase.lower() == 'fim':
            break
        
        # Verifica se a frase é um palíndromo
        if verificar_palindromo(frase):
            print(f'"{frase}" é palíndromo')
        else:
            print(f'"{frase}" não é palíndromo')

# Executa o programa
if __name__ == "__main__":
    main()
