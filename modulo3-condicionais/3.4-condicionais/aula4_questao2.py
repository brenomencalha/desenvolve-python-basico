# Classificação de Filmes

# O usuário deverá inserir a avaliação de um filme qualquer, que será classificado da seguinte maneira:
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

contador = 0
while contador < 5:
    from random import choice

    filmes = ("Interstellar", "Django Livre", "Oppenheimer", "Tenet", "A Grande Aposta")
    filme = choice(filmes)

    print (f"Avalie o filme {filme} em uma escala de 1 a 5.")
    avaliacao = int(input("Avaliação: "))

    if avaliacao == 5:
        print ("Excelente!")
    elif avaliacao == 4:
        print ("Muito Bom!")
    elif avaliacao == 3:
         print ("Bom!")
    elif avaliacao == 2:
        print ("Regular.")
    else:
        print ("Ruim.")
    contador = contador + 1