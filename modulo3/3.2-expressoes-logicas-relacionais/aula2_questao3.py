#Clube juvenil de jogos de tabuleiro

#Condições de Admissão (True)

# tiver entre 16 e 18 anos
#tiver jogado pelo menos 3 jogos
#vencido pelo menos 1 jogo

#Não admissão (False)

#negrito = ("\033[1m\033[0m")

idade = int(input("Digite sua idade: "))
jogo_tabuleiro = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
jogos_vencidos = int(input("Quantos jogo já venceu? "))

if (idade >= 16 and idade <= 18) and (jogo_tabuleiro == True) and (jogos_vencidos >=1):
    ingresso = (True)
else:
    ingresso = (False)

print (f"Apto a ingressar no clube de jogos de tabuleiro: {ingresso}")

