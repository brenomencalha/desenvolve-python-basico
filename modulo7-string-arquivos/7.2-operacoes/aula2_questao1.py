mais_velha = ['',float('inf')]

for i in range (3):
    linha = input("Digite seu nome e a data do seu nascimento: ")
    primeiro_nome = linha.split()[0]
    ano_nascimento = int(linha.split('/')[-1])
    if ano_nascimento < mais_velha[1]:
        mais_velha[0] = primeiro_nome
        mais_velha[1] = ano_nascimento
print(mais_velha)
