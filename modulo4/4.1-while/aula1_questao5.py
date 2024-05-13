contador = 0 
soma = 0

while True:
    idade = int(input("Digite as idades dos participantes da pesquisa (para sair digite 0): "))

    if idade == 0:
        break
    soma += idade
    contador += 1

media = soma / contador

print (f"A média das idades dos participantes é de {media:.0f} anos.")

    
