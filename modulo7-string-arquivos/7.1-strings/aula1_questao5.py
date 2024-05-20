def contar_vogais_e_indices (frase):
    vogais = 'aeiou'
    contador = 0 
    indices = []

    for i in range (len(frase)):
        if frase[i].lower() in vogais:
            contador += 1
            indices.append (i)
    return contador, indices

# usuário digita frase
frase = input("Digite uma frase: ")

# processamento da contagem de vogais e índices

contar_vogais, contar_indices = contar_vogais_e_indices (frase)

print(f'{contar_vogais} vogais')
print(f'Índices: {contar_indices}')