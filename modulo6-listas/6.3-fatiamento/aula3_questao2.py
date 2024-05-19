# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Usando fatiamento para extrair os nomes principais
dominios = [url[4:-4] for url in urls]

# Imprimir a lista de domínios
print(dominios)
