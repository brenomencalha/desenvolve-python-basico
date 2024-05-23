#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

import os, re

#Ler o conteúdo do arquivo frase.txt
nome_arquivo = 'frase.txt'
with open (nome_arquivo, 'r') as fp:
    conteudo = fp.read()

# Remover espaços em branco e caracteres não alfabéticos
conteudo_limpo = re.sub(r'[^A-Za-z\s]', '', conteudo)

# Dividir o conteúdo em palavras
palavras = conteudo_limpo.split()

# Salvar palavras no arquivo "palavras.txt"
nome_arquivo_palavras = 'palavras.txt'

with open(nome_arquivo_palavras,'w', encoding='utf-8') as fp_palavras:
    for palavra in palavras:
        fp_palavras.write(palavra+'\n')

# Imprimir o conteúdo do arquivo "palavras.txt"
with open(nome_arquivo_palavras,'r') as fp_palavras:
    conteudo_palavras = fp_palavras.read()
    print('Conteúdo palavras "palavras.txt": ')
    print(conteudo_palavras)