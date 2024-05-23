#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 

#Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

##Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# 1- O texto das primeiras 25 linhas
# 2- O número de linhas do arquivo
# 3- A linha com maior número de caracteres
# 4- O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

nome_arquivo = "estomago.txt"

def processar_arquivo (nome_arquivo):
    with open(nome_arquivo,'r') as file:
        linhas = file.readlines()

    # texto das primeiras 25 linhas
    print("Primeiras 25 linhas do arquivo: ")
    for linha in linhas[:25]:
        print(linha.strip())
    
    # quantidade de linhas do arquivo
    num_linhas = len(linhas)
    print(f'\nNúmero total de linhas: {num_linhas}')

    # linha com maior número de caracteres
    linha_maior = max(linhas, key=len)
    print(f'\nLinha com maior número de caracteres ([len(linha_maior)] caracteres): \n{linha_maior.strip()}')

    # número de menções aos personagens "Nonato" e "Íria"
    count_nonato = sum(1 for linha in linhas if 'nonato' in linha.lower())
    count_iria = sum(1 for linha in linhas if 'íria' in linha.lower() and 'iria' not in linha.lower())
    print(f'\nNúmero de menções a "Nonato": {count_nonato}')
    print(f'Número de menções a "Íria": {count_iria}')

processar_arquivo(nome_arquivo)


