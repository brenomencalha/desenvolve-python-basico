# Entrada da frase
frase = input("Digite uma frase: ")

# Definição vogais e consoantes:

vogais = 'aeiouAEIOU'
consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# Criação da lista de vogais e a ordena:

list_vogais = sorted([carac for carac in frase if carac in vogais])

list_consoantes = sorted([carac for carac in frase if carac in consoantes])

# Impressão das listas (vogais e consoantes):

print (f'Vogais: {list_vogais}')
print (f'Consoantes: {list_consoantes}')