#RPG - Regras
#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pontos_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if (classe == "mago") and (pontos_forca <= 10) and (pontos_magia >= 15):
    classe_escolhida = True

elif (classe == "guerreiro") and (pontos_forca >= 15) and (pontos_magia <= 10):
    classe_escolhida = True

elif (classe == "arqueiro") and (pontos_forca > 5 and pontos_forca <= 15) and (pontos_magia >5 and pontos_magia <= 15):
    classe_escolhida = True
else:
    classe_escolhida = False

print (f"Pontos de atributo consistentes com a classe escolhida: {classe_escolhida}")


