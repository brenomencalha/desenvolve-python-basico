# Em continuidade a questão 1, se pelo menos uma pessoa for maior de idade poderá ser responsável pela (s) outra (s) sendo permitida a permanência no bar

idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

if idade_juliana > 17 or idade_cris > 17:
    print ("True")
else:
    print ("False")