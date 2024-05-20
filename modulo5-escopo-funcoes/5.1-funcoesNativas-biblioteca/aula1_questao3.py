#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

import random

numero = random.randint(0,10)

while True:

    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    

    if palpite == numero:
        break

    elif palpite > 10:
        print("Entrada inválida. Digite um número entre 0 e 10 para continuar.")
            
    elif palpite > numero:
        print("Muito alto, tente novamente!")
                
    else:
        print("Muito baixo, tente novamente!")
    

print ("Parabéns! Você acertou.")