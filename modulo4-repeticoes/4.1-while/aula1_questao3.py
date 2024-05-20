n1 = int(input("Digite a nota alcançada na primeira prova deste semestre: "))
n2 = int(input("Digite a nota alcançada na segunda prova deste semestre: "))
n3 = int(input("Digite a nota alcançada na terceira prova deste semestre: "))

m = (n1 + n2 + n3)/3

if m >= 60:
    print ("Aprovado")
    print ("Fim!")

elif m >= 40:
    print ("Recuperação")
    print ("Fim!")
else:
    print ("Reprovado!")
    print ("Fim!")



