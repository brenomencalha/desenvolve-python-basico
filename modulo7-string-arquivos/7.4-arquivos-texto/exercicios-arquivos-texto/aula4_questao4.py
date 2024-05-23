import random

def escolher_palavra(palavras):
    return random.choice(palavras)

def ler_palavras():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip() for palavra in palavras]

def escolher_palavra(palavras):
    return random.choice(palavras)

def imprime_enforcado(tentativas):
    estagios_enforcado = [
        '''
         _____
        |     |
        |     
        |    
        |    
        |    
        |
        ''',
        '''
         _____
        |     |
        |     O
        |    
        |    
        |    
        |
        ''',
        '''
         _____
        |     |
        |     O
        |     |
        |    
        |    
        |
        ''',
        '''
         _____
        |     |
        |     O
        |    /|
        |    
        |    
        |
        ''',
        '''
         _____
        |     |
        |     O
        |    /|\\
        |    
        |    
        |
        ''',
        '''
         _____
        |     |
        |     O
        |    /|\\
        |    / 
        |    
        |
        ''',
        '''
         _____
        |     |
        |     O
        |    /|\\
        |    / \\
        |    
        |
        '''
    ]
    print(estagios_enforcado[tentativas])

def jogo_forca():
    palavras = ler_palavras()
    palavra_escolhida = escolher_palavra(palavras)
    tamanho_palavra = len(palavra_escolhida)
    letras_restantes = tamanho_palavra
    letras_reveladas = ["_"] * tamanho_palavra
    tentativas = 0
    tentativas_maximas = 6

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem", tamanho_palavra, "letras.")
    print("".join(letras_reveladas))  # Exibe a palavra oculta inicialmente

    while letras_restantes > 0 and tentativas < tentativas_maximas:
        letra = input("Digite uma letra: ").lower()  # Recebe uma letra do jogador

        if letra in palavra_escolhida:
            # Atualiza as letras reveladas com a letra correta
            for i, char in enumerate(palavra_escolhida):
                if char == letra:
                    letras_reveladas[i] = letra
                    letras_restantes -= 1  # Diminui o número de letras restantes

            print("".join(letras_reveladas))  # Exibe o progresso do jogador
        else:
            tentativas += 1
            print("Letra incorreta!")
            imprime_enforcado(tentativas)  # Exibe o enforcado correspondente ao número de erros

    if letras_restantes == 0:
        print("Parabéns! Você ganhou!")
    else:
        print("Você perdeu! A palavra era:", palavra_escolhida)

# Inicia o jogo
jogo_forca()
