# programa para ler as dimensões de um terreno em inteiros (comprimento e largura), e o preço do metro quadrado da região em float. Calcular o valor do terreno e imprimir o resultado .format.

comprimento = int(input("Forneça o comprimento do terreno:"))
largura = int(input("Forneça a largura do terreno:"))
preco_m2 = float(input("Preço do metro²:"))

area_m2 = comprimento * largura
preco_total =  preco_m2 * area_m2

print (f"O terreno possui {area_m2}m² e custa R$ {preco_total:,.2f}")