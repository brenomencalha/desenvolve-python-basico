# Abra o arquivo "spotify-2023.csv" para leitura
with open("spotify-2023.csv", "r", encoding='latin-1') as arquivo:
    # Leia as cinco primeiras linhas para entender a estrutura do arquivo
    for _ in range(5):
        print(arquivo.readline().strip())

# Reinicie o ponteiro do arquivo para o início
arquivo.seek(0)

# Lista para armazenar as músicas mais populares
musicas_populares = []

# Leia cada linha do arquivo
for linha in arquivo:
    # Divida a linha em colunas
    colunas = linha.strip().split(',')

    # Extraia as informações relevantes
    track_name = colunas[0]
    artist_name = colunas[1]
    released_year = int(colunas[3])
    streams = int(colunas[8])

    # Verifique se o ano de lançamento está entre 2012 e 2022
    if 2012 <= released_year <= 2022:
        # Verifique se há apenas um artista listado
        if int(colunas[2]) == 1:
            # Adicione as informações à lista de músicas populares
            musicas_populares.append([track_name, artist_name, released_year, streams])

# Imprima a lista de músicas populares
print(musicas_populares)
