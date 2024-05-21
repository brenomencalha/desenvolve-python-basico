import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            return palavra[0] + ''.join(meio) + palavra[-1]
        return palavra

    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    frase_embaralhada = ' '.join(palavras_embaralhadas)
    return frase_embaralhada

# Exemplo de uso
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
