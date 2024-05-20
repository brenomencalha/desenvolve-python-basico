# Cálculo do Frete - Entrega Expressa

# até 100km -> R$ 1,00 por kg
# entre 101 até 300km -> R$ 1,50 por kg
# > 300 km -> R$ 2,00 por kg

# Taxa de R$ 10,00 para pacotes com peso superior a 10 kg

distancia = int(input("Informe a distância em km: "))
peso = int(input("Informe o peso do pacote em kg: "))

frete = 0

if peso >= 10:
    frete = frete + 10

if distancia <= 100:
    frete = frete + (peso * 1)
elif distancia < 300:
    frete = frete + (peso * 1.5)
else:
    frete = frete + (peso * 2)

print (f"O valor do frete é R$ {frete:.2f}")
