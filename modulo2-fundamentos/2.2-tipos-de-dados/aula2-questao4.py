conta_poupanca = 500
juros = 1.01

conta_poupanca = conta_poupanca * juros# rendimento1
print ("R$", conta_poupanca)
conta_poupanca = conta_poupanca * juros # rendimento2
print ("R$", conta_poupanca)
conta_poupanca = conta_poupanca * juros # rendimento3
print ("R$", conta_poupanca)

print (f'Após 3 meses menu novo saldo é R$ {conta_poupanca:.2f}')