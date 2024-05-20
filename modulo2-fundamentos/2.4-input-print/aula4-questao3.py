# Aqui repetimos a entrada 3 vezes

qtd_vendas = 1
total_vendas = 0
while qtd_vendas < 4:
    nome_produto = input(f"Digite o nome do produto {qtd_vendas}:")
    preco_unit = float(input(f"Digite a quantidade do produto {qtd_vendas}:"))
    qtd_produto = int(input(f"Digite a quantidade do produto {qtd_vendas}:"))
    
    total_vendas = total_vendas + (qtd_produto * preco_unit)
    qtd_vendas+=1

print (f"Total: R${total_vendas:,.2f}")