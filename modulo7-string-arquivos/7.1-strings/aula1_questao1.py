def escada_de_nome():
    nome = input("Digite seu nome: ")
    
    for i in range(1, len(nome) + 1):
        print(nome[:i])

# Chamada da função para executá-la
escada_de_nome()
