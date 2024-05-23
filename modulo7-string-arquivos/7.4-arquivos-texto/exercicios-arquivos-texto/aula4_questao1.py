# Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.

import os

frase = input("Digite uma frase: ")

# salvar em um arquivo "frase.txt"
nome_arquivo = 'frase.txt'

with open(nome_arquivo, 'w', encoding='utf-8') as fp:
    fp.write(frase)

caminho_completo = os.path.abspath(nome_arquivo)
print(f'O arquivo foi salvo em: {caminho_completo}')


        