#Organização de experimentos (cobaias: sapos, coelhos, ratos)

#quantidade de experimentos
n = int(input("Digite a quantidade de experimentos: "))

soma = 0
soma_sapos = 0
soma_ratos = 0
soma_coelhos = 0
total_cobaias = 0

while soma < n:

    
    tipo_cobaia = input("Digite o tipo de cobaia (S: sapo, R:rato ou C:coelho): ")
    qtd_cobaia = int(input("Informe a quantidade de cobaia usada em cada experimento: "))

    total_cobaias = total_cobaias + qtd_cobaia
    
    if tipo_cobaia == "S":
        
        #total sapos
        qtd_sapos = qtd_cobaia
        soma_sapos += qtd_sapos
        
        soma += 1

    elif tipo_cobaia == "R":

        #total ratos
        qtd_ratos = qtd_cobaia
        soma_ratos += qtd_ratos

        soma += 1
    
    elif tipo_cobaia == "C":

        #total coelhos
        qtd_coelhos = qtd_cobaia
        soma_coelhos += qtd_coelhos

        soma += 1
    
    #percentual coelhos
    percent_coelhos = (soma_coelhos / total_cobaias) * 100
    #percentual ratos
    percent_ratos = (soma_ratos / total_cobaias) * 100
    #percentual sapos
    percent_sapos = (soma_sapos / total_cobaias) * 100

#saídas

print (f"Total: {total_cobaias:.0f} cobaias.")
print (f"Total de coelhos: {soma_coelhos:.0f}")
print (f"Total de ratos: {soma_ratos:.0f}")
print (f"Total de sapos: {soma_sapos:.0f}")
print (f"Percentual de coelhos: {percent_coelhos:.2f} %")
print (f"Percentual de ratos: {percent_ratos:.2f} %")
print (f"Percentual de sapos: {percent_sapos:.2f} %")
    






